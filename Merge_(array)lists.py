def merge_list(list1, list2):
    merged_data= ""
    #write your logic here
    if(len(list1)==len(list2)):
        for i in range(0,len(list1)):
            if(list1[i] is None):
                merged_data = merged_data +" "+ list2[(len(list2) - 1) - i]

            elif(list2[(len(list2)-1)-i]is None):
                merged_data = merged_data +" "+ list1[i]

            else:
                merged_data =merged_data+" "+(list1[i]+list2[(len(list2)-1)-i])

    resultant_data= merged_data
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)