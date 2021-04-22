#A non empty string input_str containing only brackets (,),{},[] it return output_str based on following,
#input_str is properly nested then return 0
#input_str not properly nested,return position of element in input_str -n+1

string='{{{[[()]}}}'
stack=[]
counter=0
for i in string:
    if (i=='{' or i=='[' or i=='('):
        stack.append(i)
        counter+=1
        continue

    if len(stack)==0:
        print(counter+1)
        exit()

    j=stack.pop()

    if (i=='}' and j=='{'):
        counter+=1
    elif (i==']' and j=='['):
        counter+=1
    elif (i==')' and j=='('):
        counter+=1

if len(stack)==0:
    print("Balanced")
else:
    print(counter+1)



