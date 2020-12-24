x=[2,3,4,5,6,7,8,9]
def even(n):
    for i in x:
        if i%2==0:
            print(i)
print(even(x))
#ByFilterMapReduce
l=list(map(lambda n:pow(n,2),x))
print(l)































