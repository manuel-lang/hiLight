import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import time
import threading

import demo_person as demo_logic

USE_SENSORS = False

cert_path = "certificates"
HOST_NAME = "a2k3i43s7frss9-ats.iot.eu-central-1.amazonaws.com"
ROOT_CA = f"{cert_path}/AmazonRootCA1.pem"
PRIVATE_KEY = f"{cert_path}/private.pem.key"
CERT_FILE = f"{cert_path}/certificate.pem.crt"


def windowCallback(client, userdata, message):
    print(" -> 'window': ", message.payload)
    
def send_sensor_data(brightness, temeperature=None):
    message = '{"temperature": "0", "brightness": %d}' % brightness
    
    if myAWSIoTMQTTClient.publish("sensor_data", message, 0):
        print(" <- sensor_data: %s" % message)
    else:
        print("!!!  Error sensor -> AWS IoT")

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
    sensors = Sensor(myAWSIoTMQTTClient) if USE_SENSORS else None

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

