x=list((1,2,3))
print(x)

#creating a class
class addition():
    def add_numbers(self,a,b):   #when a function is defined inside a class it is called a method
        print(a+b)
x=addition() #creating an object x
x.add_numbers(5,5)#Method being called

#To define attributes
class person:
    def __init__(self,name,age,gender): #init is used to create attributes in class
        self.name=name
        self.age=age
        self.gender= gender
p1=person('Aniruddha',19,'Male')
print(p1.name,p1.age,p1.gender)

s=str("Hello World. Send Help")
x=int(1000)

str.__add__('Hello','World')
int.__sub__(5,5)
int.__eq__(3,4)

class student:

    school= "Vikhe Patil Memorial School" #class/static variable
    def __init__(self,name,age,m1,m2):
        self.name =name
        self.age=age
        self.m1=m1
        self.m2=m2
    def student_details(self):   #self is a pointer
        print(self.name,self.age)
    def compare(self,other):                                         #other is used to compare object with another object
        total1=self.m1+self.m2
        total2=other.m1+other.m2

        if total1>total2:
            print(self.name ,"has greater marks than", other.name)
        else: print(self.name ,"has greater marks than", other.name)

s1=student("sameer",18,32,36)
s2=student("arun",18,34,38)
s3=student("vishal",20,32,21)

s1.compare(s2)
s2.compare(s3)
s1.compare(s3)
student.student_details(s1) #here s1 is pointed
s1.student_details() #here s1 goes into the function due to the pointer it accesses class variablesnot







