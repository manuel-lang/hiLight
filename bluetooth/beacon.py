import requests
import time
import json

# defining the api-endpoint  
API_ENDPOINT = "https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/activeuser"

while True:
    # TODO: PUT OWN CODE HERE
    active_user = "Alan"
    message = {"username": active_user}
    print(message)
    time.sleep(1)
    continue
    
    response = requests.post(url = API_ENDPOINT, data = data)
    print(response)

    time.sleep(1)

