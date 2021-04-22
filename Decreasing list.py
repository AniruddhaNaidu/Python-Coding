def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    try:
        for i in range(start,end+1):
            if(list1[i]>list1[i+1] and (i+1)<(end+1)):
                return i+1
                break
    except IndexError:
        print("Error")

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)