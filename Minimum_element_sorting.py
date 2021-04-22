def find_next_min(num_list, start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    min = num_list[start_index]
    for i in range(0,len(num_list)):
        if(num_list[i]<=num_list[start_index]):
            min = num_list[i]
            start_index=i

    return num_list.index(min)





#Pass different values to the function and test your program
num_list = [11, 5 ,6 , 9, 10]
start_index = 2
print("Index of the next minimum element is", find_next_min(num_list, start_index))