#$hffdsg@fshj*sj

str1=str(input())
str2=[i for i in str1 if i.isalpha()][::-1]
for i in range(len(str1)):
    if not (str1[i].isalpha()):
        str2.insert(i,str1[i])

print("".join(str2))


