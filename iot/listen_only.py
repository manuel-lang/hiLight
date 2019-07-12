import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import os
import time
import threading
import json

import demo_person as demo_logic

USE_SENSORS = 1

cert_path = "certificates"
HOST_NAME = "a2k3i43s7frss9-ats.iot.eu-central-1.amazonaws.com"
ROOT_CA = "{}/AmazonRootCA1.pem".format(cert_path)
PRIVATE_KEY = "{}/private.pem.key".format(cert_path)
CERT_FILE = "{}/certificate.pem.crt".format(cert_path)

window_mapping = {
    "0": 0,
    "1": 7,
    "2": 5,
    "3": 10,  # TODO
    "4": 7,
    "5": 10  # TODO
}

def windowCallback(client, userdata, message):
    #print(" -> 'window': {}".format(message.payload))
    windows = json.loads(message.payload.decode('utf-8'))
    
    for window in windows:
        window_id = window_mapping[window]
        reversed = 100 - windows[window]
        color = hex(int(reversed*2.5))[2:]
        
        command = 'knxtool groupwrite ip: 1/1/{} {}'.format(window_id, color)
        os.system(command)
        #print(" ----> WINDOW: {}".format(command))
    
def send_sensor_data(brightness, temeperature=None):
    message = '{"temperature": "0", "brightness": %d}' % brightness
    
    if myAWSIoTMQTTClient.publish("sensor_data", message, 0):
        #print(" <- sensor_data: %s" % message)
        pass
    else:
        #print("!!!  Error sensor -> AWS IoT")
        pass

# Connect to AWS
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("RaspberryPi")
myAWSIoTMQTTClient.configureEndpoint(HOST_NAME, 8883)
myAWSIoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)
myAWSIoTMQTTClient.connect()
print("Connection successful!")

# subscribe windows topic callback
myAWSIoTMQTTClient.subscribe("windows", 0, windowCallback)

# start face detection
interrupt_event = threading.Event()
detection_thread = threading.Thread(target=demo_logic.start, args=(myAWSIoTMQTTClient,interrupt_event))
detection_thread.start()

# set up serial interface to arduino
if USE_SENSORS:
    import read_sensor
    sensors = read_sensor.Sensors(myAWSIoTMQTTClient) if USE_SENSORS else None

# main loop
try:
    while True:
        brightness = sensors.read_sensor_data() if USE_SENSORS else 4
        send_sensor_data(brightness)
        time.sleep(1)
        
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    interrupt_event.set()  # interrupt face detection
    sensors.close()  # close serial interface
    exit(0)

