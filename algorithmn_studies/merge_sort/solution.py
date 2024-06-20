# divide and conquer the algorithm divides the array into 2 and 
# then sorts the one on the left first, until reaching where the
# array is of size 1. Making the comparison to change the positions 
# if necessary, after the left side is complete it does the right and 
# with Once done, it will compare and insert the 2 separate arrays on 
# the right and left until it is sorted.

def merge_sort(array: list):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    i = j = k = 0

    merged_array = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_array.append(left_half[i])
            i += 1
        else:
            merged_array.append(right_half[j])
            j += 1
        k += 1

    while i < len(left_half):
        merged_array.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged_array.append(right_half[j])
        j += 1

    return merged_array

if __name__ == '__main__':
    desorded_array = [20, 4, 67, 12, 40, 1, 0, 190]
    sorted_array = merge_sort(desorded_array)
    print(sorted_array)
