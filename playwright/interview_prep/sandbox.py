#first two number

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