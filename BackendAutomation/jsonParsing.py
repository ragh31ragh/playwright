import json
#loads method for string
#load for json file object
courses = '{"name" : "RahulShetty" , "Languages" : ["Java","Python"]}'
dict_courses = json.loads(courses)
print(dict_courses["name"])
print(dict_courses["Languages"][0])

with open ('C:\\RD\\Trainings\\2025_API_Testing\\course.json') as f :
    data = json.load(f)
    print(data)
    print(data['dashboard']['website'])
    print(data['courses'][1]['title'])

##finding price of course RPA
    for course in data['courses']:
        print(course)
        if course['title'] == "RPA" :
            print(f"Price of course RPA {course['price']}")

with open ('C:\\RD\\Trainings\\2025_API_Testing\\course1.json') as fi :
    data1 = json.load(fi)
    print (data1 == data )
    assert data1 == data