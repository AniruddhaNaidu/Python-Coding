#Given a list (combination of repeated and distinct
#elements which are space separated) and number of elements deletion X.
#You have to delete any X element from the list so that list will have minimum no of distinct numbers.
#sample_input= 4
#              1112233456    (4,5,6,(any of the recurring number) will get deleted to have 1,2,3 as i.e 3 distinct elements)
#sample_output=3

X=int(input())
l1=list(map(int,input()))
unique=list(set(l1))
f=[]
for i in unique:
    elem=[i]*l1.count(i)
    f=f+elem

result=sorted(f, key = f.count)
l2=result[X:len(result)]
min_dis=list(set(l2))
print(len(min_dis))
