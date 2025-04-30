import requests
#response=requests.get("https://reqres.in/api/users?page=2")
response = requests.get("http://216.10.245.166/Library/GetBook.php",
             params={"AuthorName":"Rahul Shetty2"},)
json_response = response.json()
print(type(json_response))
print(json_response)
assert  response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8' , "ExpectedValueDidNotMatch"
#Retrieve the book details with bnid3473
#print(json_response[6]['book_name'])
for items in json_response:
    #print(items)
    #print(items['book_name'])
    if items['isbn'] == '0108':
        print(items['book_name'])
        break