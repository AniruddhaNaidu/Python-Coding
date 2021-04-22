#find longest substrinfg of unique characters which is case insensitive
#if length of subset is less than 3 then print -1

str1=input()
substr=''.join(list(dict.fromkeys(str1)))
sub_list=[]
for i in range(0,len(substr)):
    for j in range(i,len(substr)):
        sub_list.append(substr[i:j+1])

sub_list=sorted(set(sub_list),key=len)[::-1]

t_sub=[]
sub=''
for i in sub_list:
    if str1.count(i)==1:
        sub=''.join(i)
        break

if len(sub)<3:
    print(-1)
else:
    print(sub)