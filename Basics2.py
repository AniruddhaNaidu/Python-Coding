y=[3,5,True,0.3,-2,8+6j]

for i in y:
    print(i+1)

dict={
    'messi' : 'football',
    'virat' : 'cricket',
     'sindhu' : 'badminton'

}
i=0
while i<len(dict):
    for i,j in dict.items():
        print(i,j)
    break



dict.items()
for i,j in dict.items():
    print(i,j)

for i in dict.values():
    print(i)

x=[1,2,3,4,6,7,8,9]
for i in x:
    if i>5:
        print(i)

x=[2,3,4,6,11,10]
i=0
while i<len(x):
    print(x[i])
    i=i+1

x=int(input("enter no"))
if x>0 and x%2==0 :
    print(x, 'is even no')

elif x>0 and x%2!=0:
    print(x, 'odd number')
elif x<0:
    print(x, 'negative number')


range(10)

for i in range(10):
    print(i)

