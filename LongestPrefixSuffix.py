#Given a string s, find length of the longest prefix which is also suffix.
# The prefix and suffix should not be overlap.
#sample input= abcdabc
#sample output= (abc->)3
string= list(input())
mid=len(string)//2
l=0
for i in range(mid,0,-1):
    suf=string[0:i]
    pref=string[len(string)-i:len(string)]
    if suf==pref and len(suf)>l:
        l=len(suf)

print(l)