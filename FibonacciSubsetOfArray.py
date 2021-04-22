#Given an array with positive number(comma separated) the task is that
#we find largest subset from array that contain elements which are Fibonacci Numbers.
#If more than two elements exist then print its length else print -1.
arr=sorted(list(map(int,input().split(","))))
max=arr[len(arr)-1]
a=0
b=1
c=0
fibb=[a,b]
while(max>=c):
    c=a+b
    fibb.append(c)
    a=b
    b=c

count=0
unique_arr=list(dict.fromkeys(arr))
if arr.count(1)==2:
    unique_arr.append(1)
unique_arr=sorted(unique_arr)
sub=[]
for i in set(fibb):
    for j in unique_arr:
        if j==i:
            count+=1
            sub.append(j)

if sub.count(1)<2:
    sub.remove(0)
    count=count-1

sub=sorted(sub)

if count>=2:
    print(sub)
else:
    sub.clear()
    sub.append(-1)
    print(sub)