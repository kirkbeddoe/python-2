# create a merge sort function

def merge_sort(list_1):
    # base case
    if len(list_1) <= 1:
        return list_1

    mid = len(list_1) // 2 # find the middle index

    # divide the list into two halves
    left_half = merge_sort(list_1[:mid])
    right_half = merge_sort(list_1[mid:])

    # merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # compare elements from both halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1

        else:
            sorted_list.append(right[j])
            j += 1

    # add any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

strings = ["banana", "apple", "orange", "berry", "grape"]
sorted_strings = merge_sort(strings)
print("Sorted List: ", sorted_strings)


