# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import requests
import time
import json

import bluetooth._bluetooth as bluez

API_ENDPOINT = "https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/activeuser"

ids = {
    "fda50693a4e24fb1afcfc6eb07647825": "Alan",
    "5da1ef28d3af4a87b66e568cc1e2ec9d": "Arne"
}

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	for beacon in returnedList:
        split = returnedList.split(",")
        beacon_id = split[1]
        if beacon_id in ids and abs(int(split[-1])) < 40:
            active_user = ids[beacon_id]
            data = {"username": active_user}
            
            print("Sending")
            response = requests.post(url = API_ENDPOINT, data = data)
            print(response)

