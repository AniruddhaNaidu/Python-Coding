#Take a string as input, separate all the integers from it,
# Then take each integer only once and form a largest even number possible.
# Print largest even number possible and if the number can't be made, then print -1.

string=input()
num_list=[]
for i in range(0,len(string)):   #list(set(re.findall('\d', test_string)))
    if (string[i].isdigit()):
        num_list.append(string[i])

digits=list(dict.fromkeys(sorted(num_list,reverse=True)))
number=int(''.join(digits))
if number%2==0:
    print(number)
else:
    for i in range(len(digits)-1,0,-1):
        if int(digits[i])%2==0:
            e=digits[i]
            digits.remove(e)
            digits.insert(len(digits),e)
            even=int("".join(digits))
            print(even)
            break

print(number)

