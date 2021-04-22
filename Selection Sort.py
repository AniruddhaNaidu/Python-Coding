# lex_auth_0127667356693872643343

def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


def find_next_min(num_list, start_index):
    min = num_list[start_index]
    for i in range(start_index, len(num_list)):
        if (num_list[i] <= num_list[start_index]):
            min = num_list[i]
            start_index = i

    return start_index


def selection_sort(num_list):
    for i in range(len(num_list) - 1):
        start_index = i
        second_index = find_next_min(num_list, start_index)
        swap(num_list, start_index, second_index)


num_list = [8, 2, 19, 34, 23, 67, 91]
print("Before sorting;", num_list)
selection_sort(num_list)
print("After sorting:", num_list)