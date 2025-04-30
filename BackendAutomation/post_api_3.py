#import configparser
import requests
#config = configparser.ConfigParser()
#config.read('utilities/properties.ini')
from utilities.configurations import getConfig
from utilities.resources import *

url = getConfig()['API']['endpoint']+ApiResources.getUsers
payload={
    "name":"Raghavendra",
    "job" : "Automation"
}

response = requests.post(url,data=payload)
print(response.json())
print(response.status_code)
assert response.status_code == 201 , "response status code is not 200"