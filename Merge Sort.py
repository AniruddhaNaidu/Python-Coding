# lex_auth_0127667368801157123532

def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low = 0
    high = len(num_list) - 1
    mid = (low + high) // 2
    left_list = num_list[low:mid]
    right_list = num_list[mid+1:high]
    if high <= low:
        return
    else:
        merge_sort(left_list)
        merge_sort(right_list)
        sl= merge(left_list, right_list)
        return sl


def merge(left_list, right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i = 0
    j = 0
    sl = []
    while (i < len(left_list) and j < len(right_list)):
        if (left_list[i] <= right_list[j]):
            sl.append(left_list[i])
            i += 1
        else:
            sl.append(right_list[j])
            j += 1

    if not left_list:
        sl.extend(left_list)

    if not right_list:
        sl.extend(right_list)

    return sl


num_list = [34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:", num_list)
sorted_list = merge_sort(num_list)
print("After sorting:", sorted_list)
