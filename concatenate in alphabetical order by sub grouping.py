str1='HelLo WORLd Dog'
list2=[]
for i in (sorted(set(str1.casefold()))):
    list1=[]
    if i == ' ':
        continue
    for j in (sorted(set(str1))):
        if i.casefold()==j.casefold():
            list1.append(j)
            list2.extend(sorted(list1))
    print("Group %s: "%i,list1)

print(list2)

