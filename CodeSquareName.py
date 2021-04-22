#Take input from the user in the given format(consist of name and code).
#Find the sum of square of digits from code.
#If the sum of squares of digits of the code are :
#EVEN:- Then add the last 2 characters in the beginning
#ODD:- Then add first character at the end

string= 'Anchal:2,Brijesh:3,Rohit:57234,Aman:5,Sonakshi:4'
list1=string.split(",")
out_str=''
for i in list1:
    name, num = i.split(':')
    l=len(name)
    sum = 0
    for digit in num:
        sum+=(int(digit))**2

    if sum%2==0:
        out_str+=name[l-2:l]+name[0:-2]+" "

    else:
        out_str+=name[1:l]+name[0]+" "

print(out_str)



