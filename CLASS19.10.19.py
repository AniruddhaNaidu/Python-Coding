#CREATING A CLASS WITHIN A CLASS
class student:
    def __init__(self,age):
        self.age=age
        self.l2= self.laptop("Ankur","Dell","4GB","i5")#CREATING AN OBJECT OF INNER CLASS INSIDE THE OUTER CLASS __init__ FUNCTION


    class laptop:
        def __init__(self,name,compname,ram,cpu):
            self.name=name
            self.compname=compname
            self.ram=ram
            self.cpu=cpu
        def laptop_details(self):
            print("The student ",self.name," has ",self.compname, "laptop with configuration" , "RAM:", self.ram,"CPU:", self.cpu)
    l1=laptop("Ankur","Dell","4GB","i5")

s1=student(29)
s1.l1.laptop_details() #CALLING METHOD 1
student.laptop.laptop_details(s1.l1)#CALLING METHOD 2
lappy1=student.laptop("Ankur","Dell","4GB","i5")
lappy1.laptop_details()#CALLING METHOD 3
s1.l2.laptop_details()#CALLING METHOD 4