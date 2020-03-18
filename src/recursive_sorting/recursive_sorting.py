# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # merge arrays without sorting so we can pop their values
    initial_merge = arrA + arrB

    # loop over each index in the placeholder array and replace their values
    for i in range(0, len(merged_arr)):
        # initialize our smallest index with the first item
        smallest_index = 0

        # get smallest value from unsorted list
        for n in range(0, len(initial_merge)):
            if initial_merge[n] < initial_merge[smallest_index]:
                smallest_index = n
        merged_arr[i] = initial_merge.pop(smallest_index)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print("Initial Arr", arr)
    # base case, if array length is 1, it's sorted and should be returned
    if len(arr) <= 1:
        return arr

    # split list in half
    left_side = arr[len(arr) // 2 :]
    right_side = arr[: len(arr) // 2]
    # recursively sort left and right sides
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    arr = merge(left_side, right_side)
    print("Sorted Arr", arr)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
