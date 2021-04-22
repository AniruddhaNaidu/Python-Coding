import itertools

l1=list(map(int,input().split(",")))
sum=0
for i in l1:
    sum=sum+i

l2=list(itertools.combinations(l1,4))

combo_list=[]
for i in l2:
    sum2=0
    for j in i:
        sum2+=j
    if(sum2==sum):
        combo_list.append(i)

print(combo_list)