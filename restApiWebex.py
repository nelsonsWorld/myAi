import requests
import os
import json
import pprint

# Get environment variables
#https://restful-api.dev/
ACCESS_TOKEN = os.getenv('WEBEX_ACCESS_TOKEN')

pp = pprint.PrettyPrinter(indent=4)

url = "https://webexapis.com/v1/rooms"

payload={}

headers = {

  'Authorization': 'Bearer ' + ACCESS_TOKEN

}

response = requests.request("GET", url, headers=headers, data=payload)

json_response = json.loads(response.text)

pp.pprint(json_response)
    
    