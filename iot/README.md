# IoT (Raspberry Pi Sensors)

To run the scripts you will need to pip the *requirements.txt* file.

## 

```python
# The unique hostname that AWS IoT generated for this device.
HOST_NAME = "a2k3i43s7frss9-ats.iot.eu-central-1.amazonaws.com"

# The relative path to the correct root CA file for AWS IoT.
ROOT_CA = "certificates/AmazonRootCA1.pem"

# The relative path to your private key.
PRIVATE_KEY = "certificates/private.pem.key"

# The relative path to your certificate file of this device
CERT_FILE = "certificates/certificate.pem.crt"
```

## Commands

Important commands are:

```python
# Set up the connection to AWS IoT
myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient("RaspberryPi")
myAWSIoTMQTTClient.configureEndpoint(HOST_NAME, 8883)
myAWSIoTMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)
myAWSIoTMQTTClient.connect()
```

```python
def callback(client, userdata, message):
    print(message.payload)

# Subscribe to a topic, the callback function is called when something is published to the topic
myAWSIoTMQTTClient.subscribe("topic_name", 0, callback)
```

```python
# Publish to a topic
success = myAWSIoTMQTTClient.publish("topic_name", message, 0)
```