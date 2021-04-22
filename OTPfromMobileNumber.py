#Input will be like 5624381275. Separate odd places integers = 6, 4, 8, 2, 5
#You have to return a 4-digit OTP by squaring the digits. Digits according
#to input are 6, 4, 8, 2, 5
#Square those numbers-36, 16, 64, 4, 25
#So, the OTP to be returned is first four digits i.e. 3616


odd_str=input()[1::2]
print(odd_str)
power=""
for i in range(0,len(odd_str)):
    power+=str((int(odd_str[i]))**2)
print(power)
print(power[0:4])