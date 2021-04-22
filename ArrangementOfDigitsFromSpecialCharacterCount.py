#Statement: Given a string containing at least one special character, one even-digit and one odd-digit,
#return an output string outstr based on the number of special characters as below:
#• If the number of special characters is odd, append all the odd digits
#  and even digits alternatively to the outstr, starting with the first odd digit.
#• If the number of special characters is even, append all the even digits and odd digits
#  alternatively the outstr, starting with the first even digit.
#• After arranging the digits based on the above two points, if there are any additional
#  digits remaining, append them at the end of outstr.
#sampleinput=A82039*#6whY8
#sampleoutput=8329068

l1=input()
spch=0
even=[]
odd=[]

for i in l1:
    if not(i.isalnum()):
        spch+=1
    if i.isdigit():
        if (int(i))%2==0:
            even.append(i)
        else:
            odd.append(i)


print(even)
print(odd)
min=len(even) if len(odd) >= len(even) else len(odd)
max=len(even) if len(odd) < len(even) else len(odd)

print(min)
print(max)
print(spch)
str=''

for i in range(0,min):
    if spch%2==0:
        str+= even[i]+odd[i]

    else:
        str+= odd[i]+even[i]

    max_list = even if len(odd) < len(even) else odd
    str=list(str)
    str.extend(max_list[min:max])

print(str)
