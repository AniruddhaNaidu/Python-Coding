def sum(x,y):
    print(x+y)


x=float(input("Enter 1st no: "))
y=float(input("Enter 2nd no: "))
sum(x,y)

import math
def fact(x):
    print(math.factorial(x))

x=int(input("Enter no: "))
fact(x)

#KEYWORD ARGUMENTS
def student(name, age):
    print(name)
    print(age+5)

student(age=27,name="amit")

#DEFAULT ARGUMENTS
def student(name="Amit", age=20):
    print(name)
    print(age+5)

student()

#VARIABLE LENGTH
def sum(*args):
     c=0
     for i in args:
         c=c+i
     print(c)

sum(2,3,4,5,5,6)


 #KEYWORD VARIABLE LENGTH
def person(name,**data):
    print(name)
    #print(data)
    for i in data.values():
        print(i)

person("Ankur",age=29,city="pune",state="maharashtra")










































