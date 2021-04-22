#A string of comma separated numbers are given such that
# the numbers 4 and 7 are already present in the list.
# Assume that 7 always comes after 4 in the given string.
input='2,4,9,5,8,7,3,2'
num_list=list(input.split(","))
print(num_list)
str=""
for i in range(num_list.index('4'),num_list.index('7')+1):
    str=str+num_list[i]

num2=int(str)
print(num2
      )

num1=0
for i in range(0,num_list.index('4')):
    num1=num1+int(num_list[i])
for i in range(num_list.index('7')+1,len(num_list)):
    num1=num1+int(num_list[i])
print(num1)

output=num1+num2