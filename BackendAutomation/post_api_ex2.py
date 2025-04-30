#import configparser
import requests
#config = configparser.ConfigParser()
#config.read('utilities/properties.ini')
from utilities.configurations import getConfig

payload={
    "name":"Raghavendra",
    "job" : "Automation"
}
#response = requests.post("https://reqres.in/api/users",data=payload)
#response = requests.post(config['API']['endpoint']+'/api/users',data=payload)
response = requests.post(getConfig()['API']['endpoint']+'/api/users',data=payload)
print(response.json())
print(response.status_code)
assert response.status_code == 201 , "response status code is not 200"