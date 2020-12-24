i=2000
x= []
while i<=3200:
    if i%7==0:
        print(i)
        x.append(i)
        i+=1
    else: i+=1
print("There are",len(x),"elements")

for i in range(2000,3201):
    if i%7==0:
        print(i)

y=[1,2,3,4,5,6]
def odd_even():
    for i in y:
         if i%2==0:
            print(i)

odd_even()
