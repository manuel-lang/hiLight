import serial


class Sensors(object):
    def __init__(myAWSIoTMQTTClient):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.myAWSIoTMQTTClient = myAWSIoTMQTTClient
        
    def read_sensor_data():
        line = self.ser.readline()
        brightness = int(line.decode("utf-8").replace("\r\n", ""))
        return brightness
    
    def close():
        self.ser.close()
