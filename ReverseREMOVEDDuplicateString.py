#Program to reverse string after removing duplicates

#Method1
in_str=input()
out_str=""
for i in in_str:
    if i not in out_str:
        out_str=out_str+i
print(out_str[::-1])

#method2
print("".join(list(dict.fromkeys(input()))[::-1]))