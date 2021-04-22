arr=input()
substr=[]
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        substr.append(arr[i:j+1])

substr=list(map(int,set(substr)))

pronic_set=[]
n=1
p_no=0
while(p_no<=int(arr)):
    p_no=n*(n+1)
    pronic_set.append(p_no)
    n+=1

pronic_no=[]
for i in substr:
    for j in pronic_set:
        if i==j:
            pronic_no.append(i)


print(sorted(set(pronic_no)))