#Take input from the user in the given format(consist of name and code).
#Find the maximum digit from code which is less than or equal to(<=)
# the length of name and put the place char in the final string if there is
# no digit found which satisfies the given condition then simply put 'X'.


string= 'Anchal:83252,Brijesh:89897,Rohit:57234,Aman:59967,Sonakshi:82834'
list1=string.split(",")
final_str=''
for i in list1:
    name,num=i.split(':')
    l=len(name)
    max=0

    for dig in num:
        if int(dig)<=l and int(dig)>=max:
            max=int(dig)

    if max==0:
        final_str+='X'
    else:
        final_str+= name[max-1]

print(final_str)




