print('hello world')
x=3
y=3
z='hello'
print(id(x*y))
print(type(z))
print(len(z))
print(2**3)

import math

x = [1,2,3,4,5,4]
print(x[1:4])
x.reverse()
x.insert(1,'Sameer')
x.count(4)
print(x)

a=(2,3.4,True,'hello')
print(a.index(3.4))

y = {
         1:  'January',
         2:  'February',
         12:  'December'
        }
print(y)
y1= y.copy()
print(y1)
print(len(y))
print(y.pop(1))
y1= y.copy()
print(y1)
print(y.popitem())
y.update({99:'July'})

s1={1,3,4,9.4}
s2={1,3,4,9.4,True}
print(s1)

x=3
if x>1:
      print(x, "greater than 1")
elif x>2:
    print(x, "greater than 2")
else:
      print(x, "less than 1")