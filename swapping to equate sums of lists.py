l1=list(map(int,input().strip().split(" ")))
l2=list(map(int,input().strip().split(" ")))

def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum


def product(list):
    even = []
    odd = []
    for i in list:
        prod = 1
        for j in i:
            prod = prod * j
        if prod % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return odd,even

sum1=sum(l1)
sum2=sum(l2)
comb_list=[]

if not (sum1==sum2):
    for  i in range(0,len(l1)):
        for j in range(0,len(l2)):
            l1[i],l2[j]=l2[j],l1[i]
            if sum(l1)==sum(l2):
                num1=l2[j]
                num2=l1[i]
                comb=[num1,num2]
                comb_list.append(comb)
            l1[i], l2[j] = l2[j], l1[i]
    if len(comb_list)==0:
        comb_list.append(-1)
    else:
        odd, even = product(comb_list)
        out_list=[]
        out_list=[sorted(even),sorted(odd)[::-1]]
        out_list.remove([])
        print(odd)
        print(even)
        print(out_list)



else:
    comb_list.append(-1)
    print(comb_list)




