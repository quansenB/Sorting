# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    count = 1
    indexOfSmallest = 0
    while count <= len(arr):
        indexOfSmallest = count - 1 
        for i in range(count, len(arr)):
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)

            if arr[indexOfSmallest] > arr[i]:
                indexOfSmallest = i

        # TO-DO: swap

        temp = arr[count-1]
        arr[count-1] = arr[indexOfSmallest]
        arr[indexOfSmallest] = temp
        count += 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    condition = True
    while condition:
        condition = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                condition = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr