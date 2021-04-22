n=68
rem_list=[]
while(n!=0):
    rem=n%2
    n=n//2
    rem_list.append(rem)
print(rem_list)


max=0
count=0
i=0
while (i<=(len(rem_list)-1)):

    if(rem_list[i]==0):
        count+=1
        if count>max:
            max=count
    else:
        count=0
    i+=1

print(max)


