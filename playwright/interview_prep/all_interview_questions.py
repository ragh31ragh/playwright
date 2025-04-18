############1.patterns############
#
##
###
####
#####
print("############1.1 patterns############")
n=5
for i in range(1,n+1):
    print("*" * i,end=" ")
    print("\t")

print("############1.2 patterns############")
n=5
for i in range(n,0,-1):
    print("*" * i,end=" ")
    print("\t")

print("############1.3 pyramid pattern############")
n=5
for i in range(1,n+1):
    print(" "* (n-i),end=" ")
    print("*" * ((2*i)-1),end=" ")### (Sequence to print odd numbers (2n-1)###
    print("\t")

print("############2 :Factorial for given number############")

def factorial_calculation(n):
    result = 1
    count =  1
    while ( count < n+1 ) :
        result = result * count
        count = count + 1
    return (result)
fact_number = input("Enter the number to calculate factorial - between 3 to 9 \n")
print(f"factorial of number {fact_number} is :::: ")
print(factorial_calculation(int(fact_number)))

print("###### 3.Count the number of vowels in string###########")

mystring="indiaa mysuru"
vowels="aeiou"
counter = 0
for char in mystring:
    if (char.lower() in vowels):
        counter = counter+1 ;
print(counter)

print("###### 4.Find the longest word in a sentence using for loop###########")
teststring = "this is python learning indiabengalurumysurumandyawww4 timeoo in laptop adfafewrww indiabengalurumysurumandya"
new_string_list = teststring.split(" ")
length_calc = 0 ;
for words in new_string_list:
    if ( len(words) > length_calc ):
        length_calc = len(words)
        longest_word = words
print("Longest word is : :::")
print(longest_word)


print("###### 5.1 lambda functions###########")
a = lambda x,y : x+y
print(a(3,4))

print("###### 5.2 map plus lambda functions###########")
numbers = [1,2,3,4,5]
qube_numbers = map(lambda x : x*3,numbers)
print(list(qube_numbers))

print("###### 5.3 filter plus lambda functions###########")
numbers1 = [1,2,3,4,5,53,67,88]
even_numbers = filter(lambda x : x%2 == 0,numbers1)
print(list(even_numbers))

print("###### 6. fibonacci series###########")
def fib(n):
    a=0
    b=1
    count = 2
    print(a)
    print(b)
    while (count < n) :
        #print(n)
        a, b = b, a + b
        print(b)
        count = count+1

fib(12)