def add(x,y):
    return x+y

print(add(3,3))
x=4
y=9

addition = lambda x,y : x + y
print(addition)
###map####
numbers=[1,2,3,4,5]
squared_numbers = map(lambda x : x*3 ,numbers)
print(list(squared_numbers))


###filter####
even_numbers = list(filter(lambda x : x%2 == 0,numbers))
print(even_numbers)

###sorting#####
sorting = [3,2,6,7,9]
print(sorted(sorting))