
def reverse(num):
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
try:

    def palindrome(num):
        sum=num+reverse(num)
        if (reverse(sum)!=sum):
            palindrome(sum)
        else:
            print("%d is a Palindrome" %sum)

except RecursionError:
    raise Exception()

try:
    palindrome(986)
except Exception:
    print("No Palindrome Found")


#alternative code
def palindrome(num):
    return str(num)[::-1]==str(num)
def reverse(num):
    return int(str(num)[::-1])

num=154#int(input())
while(1):
    num=num+reverse(num)
    if(palindrome(num)):
        print(num)
        break




