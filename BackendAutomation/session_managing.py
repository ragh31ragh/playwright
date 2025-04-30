import requests
se = requests.session()
se.auth = ("username",getPassword())
response = se.get(url, params= )