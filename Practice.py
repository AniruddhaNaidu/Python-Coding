def func(a,b):
    c=0
    if a==0:
        c+=b//2
        return 0
    elif(a%2):
        return c+func(a//2,2*b)+b
    else:
        c+=2
        return c+func(a//2,2*b)-b
print(func(24,2))