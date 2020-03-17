# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for i in range(cur_index, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # set break condition for sort
    swapped = True

    # loop through data until we don't swap any items
    while swapped is True:
        # before looping, set swapped false so we can break out of while if no items were swapped
        swapped = False

        # loop through array checking neighbors
        for i in range(0, len(arr) - 1):
            # if left > right, swap
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
