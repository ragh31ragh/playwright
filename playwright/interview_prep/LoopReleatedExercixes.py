#print("Hello",end=" ")
#print("RD")
'''

i=0
while i  < 5 :
    print("Hello RD",end=" ")
    i+= 1
'''

#2:Star pattern
#*
#**
#***
#****
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print("\t")
'''

##one more logic

n=5
for i in range(1,n+1):
    print ("*" * i)


###inverted triange
print("###########Inverted Triangle #######")
for i in range (n,0,-1):
    print("*" * i)


print("##########Pyramid Pattern #######")
####Pyramid pattern ####
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * ( 2*i -1))

print("##########Factorial #######")
#*2*1=6
num1=5
temp = 1
for i in range(1,num1+1):
    temp = temp*i
    #print(temp)
print(temp)

def factorial(n):
    result = 1
    while n>0:
        result = result * n
        n = n-1
    return result

print(factorial(3))


print("###### 4.Count the number of vowels in string###########")
my_string="python by raghavendra d aiou"
vowels="aeiou"
count = 0
for char in my_string:
    if char.lower() in vowels:
        count += 1
print(f"number of vowels in given string is {count}")


print("###### 5.Find the longest word in a sentence using for loop###########")
sentence = "Find the longest word in a sentence ewafdfasfdafsddsafdfda using for loop"
words = sentence.split(" ")
print(words)
longest_word = " "
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        #print(longest_word)
print(f"longest word in given sentence is {longest_word}")

print("###### 6.Do while loop in python and how to do it ###########")
print("###### 7.Fibonacci sequence  ###########")
def fibonacci(n):
    a,b = 0,1
    count = 0
    while (count < n):
        print(a)
        a,b = b , a+b
        count += 1


print(fibonacci(15))