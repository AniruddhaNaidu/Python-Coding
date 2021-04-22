innum= int(input())

def reverse(num):
    rev=0
    while num!=0:
        rev=(rev*10)+(num%10)
        num=num//2
    return rev

def palindrome(num):
    if num==reverse(num):
        return 1
    else:
        return 0

def lowerp(innum):
    while innum!=0:
        innum-=1
        if palindrome(innum) and innum!=0:
            num1=innum
            break
        else:
            num1=0

    return num1


def higherp(innum):
    while innum != 0:
        innum += 1
        if palindrome(innum) and innum != 0:
            num2 = innum
            break
        else:
            num2 = 0
    return num2



def sump(innum):
    num1,num2=0,0
    num1=lowerp(innum)
    num2=higherp(innum)
    s=0
    s=num1+num2
    if palindrome(s):
        outnum=s
        print(outnum)
    else:
        if innum!=0:
            innum-=1
            sump(innum)

sump(innum)