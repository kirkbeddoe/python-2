# create a quick sort function

def quick_sort(list_1):
    # base case
    if len(list_1) <= 1:
        return list_1

    pivot = list_1[-1]

    # elements smaller than pivot point leader
    # elements greater than pivot points leader
    # the pivot point itself

    left = [x for x in list_1[:1] if x < pivot]
    right = [x for x in list_1[:1] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("Sorted List: ", sorted_numbers)






