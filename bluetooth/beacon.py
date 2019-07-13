import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import time

cert_path = "certificates"
HOST_NAME = "a2k3i43s7frss9-ats.iot.eu-central-1.amazonaws.com"
ROOT_CA = "{}/AmazonRootCA1.pem".format(cert_path)
PRIVATE_KEY = "{}/private.pem.key".format(cert_path)
CERT_FILE = "{}/certificate.pem.crt".format(cert_path)

# Connect to AWS
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("BluetoothPi")
myAWSIoTMQTTClient.configureEndpoint(HOST_NAME, 8883)
myAWSIoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)
myAWSIoTMQTTClient.connect()
print("Connection successful!")

while True:
    # TODO: PUT OWN CODE HERE
    active_user = "Alan"
    message = '{"active_user": "%s"}' % active_user
    if not myAWSIoTMQTTClient.publish("bluetooth", message, 0):
        print("Could not publish to AWS IoT!")
    time.sleep(1)

