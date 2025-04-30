import requests
payload={
    "name":"Raghavendra",
    "job" : "Automation"
}
response = requests.post("https://reqres.in/api/users",data=payload)
print(response.json())
print(response.status_code)
assert response.status_code == 201 , "response status code is not 200"