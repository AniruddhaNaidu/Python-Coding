#PASS
if 32>28:
    pass
#BREAK
x=[2,3,4,5,6,7]
for i in x:
    if i == 6:
        break
    print(i)

y=[2,3,4,5,6,7]
j=0
while j<len(y):
    print(y[j])
    j = j + 1
    if y[j] == 6:
        break
#CONTINUE
x=[2,3,4,5,6,7]
for i in x:
    if i == 6:
        continue
    print(i)

y=[2,3,4,5,6,7]
j=0
while j<len(y):
    if y[j] == 6:
        j+=1
        continue
    print(y[j])
    j = j + 1


    def sum():
        print(5 + 4)
sum()