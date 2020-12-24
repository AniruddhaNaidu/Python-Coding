#FUNCTION RECURSION
import  sys
sys.setrecursionlimit(2000)
i=0
def hello():
    global i
    print("Hello",i)
    i +=1
    hello()
hello()

#Factorial
def factorial(x):
    if x==0:
        return 1
    return x* factorial(x-1)

print(factorial(5))

#Fibonnacci
a=0
b=1
def fibb(n):
    global a,b
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range (2,n):
            c=a+b
            print(c)
            a,b=b,c

fibb(7)

#Fibonacci Recursive
def fib(n):
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))
















































































































































































































