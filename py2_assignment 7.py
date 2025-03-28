# create a bubble sort

def bubble_sort(list_1):

    # get the number of elements in the list
    number = len(list_1)

    # first loop to go through all elements
    for i in range(number):
        for j in range(0, number-i-1):
            if list_1[j] > list_1[j+1]:

                # swap here
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

    return[list_1]

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list: ", sorted_numbers)



