#SINGLE LEVEL INHERITANCE
class A:
    def show_A(self):
        print("class A")

class B(A):
    def show_B(self):
        print("class B")

b1=B()
b1.show_A()

#MULTILEVEL INHERITANCE
class A:
    def show_A(self):
        print("class A")

class B(A):
    def show_B(self):
        print("class B")

class C(B):
    def show_C(self):
        print("class C")

x=C()
x.show_A()
x.show_B()
x.show_C()

#MULTIPLE INHERITANCE
class A:
    def show_A(self):
        print("class A")


class B:
    def show_B(self):
        print("class B")


class C(A,B):
    def show_C(self):
        print("class C")

y=C()
y.show_B()

#HOW CONSTRUCTOR BEHAVES IN INHERITANCE
class A:
    def __init__(self):
        print("init A")
    def show_A(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__() #init function of A is called
        print('init B')
    def show_B(self):
        print("B")


x=B() #init function of A is called by default if init isn't present in B
x.__init__()