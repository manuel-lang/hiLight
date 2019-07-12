import serial


class Sensors(object):
    def __init__(self, myAWSIoTMQTTClient):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.myAWSIoTMQTTClient = myAWSIoTMQTTClient
        
    def read_sensor_data(self):
        line = self.ser.readline()
        brightness = int(line.decode("utf-8").replace("\r\n", ""))
        return brightness
    
    def close(self):
        self.ser.close()
