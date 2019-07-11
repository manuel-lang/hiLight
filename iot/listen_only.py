import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import time

cert_path = "certificates"

# The unique hostname that AWS IoT generated for 
# this device.
HOST_NAME = "a2k3i43s7frss9-ats.iot.eu-central-1.amazonaws.com"

# The relative path to the correct root CA file for AWS IoT, 
# that you have already saved onto this device.
ROOT_CA = f"{cert_path}/AmazonRootCA1.pem"

# The relative path to your private key file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
PRIVATE_KEY = f"{cert_path}/private.pem.key"

# The relative path to your certificate file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
CERT_FILE = f"{cert_path}/certificate.pem.crt"


def windowCallback(client, userdata, message):
    print(" -> 'window': ", message.payload)

# Create, configure, and connect a shadow client.
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("LaptopTest")
myAWSIoTMQTTClient.configureEndpoint(HOST_NAME, 8883)
myAWSIoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)
myAWSIoTMQTTClient.connect()

print("Connection successful!")

myAWSIoTMQTTClient.subscribe("windows", 0, windowCallback)

while True:
    time.sleep(10)

myAWSIoTMQTTClient.disconnect()


