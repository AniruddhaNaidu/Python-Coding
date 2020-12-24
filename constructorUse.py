x=[]
x=list((1,2,3,4,5))
print(x)

x=dict(Jan="January",Feb="February")

x=list((1,2,3,4,5))
x1=[]
def passing(x):
    for i in x:
        x1.append(pow(i,2))
    print(x1)

passing(x)

x=[0,-2,-4,7,6,-7,8,10]
x1_pos=[]
x1_neg=[]
def posineg(x):
    for i in x:
        if i<0:
            #print (i,"is negative")
            x1_neg.append(i)
        elif i==0:
            print (i,"is neither negative nor positive")
        else: x1_pos.append(i)
        #print(i, "is positive")

posineg(x)
print(x1_neg,"are the negative numbers")
print(x1_pos,"are the positive numbers")





























































































































































































