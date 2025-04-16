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