# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    while len(arrA) != 0 or len(arrB) != 0:
        if bool(arrA[0]) and bool(arrB[0]):
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA.pop(0))
            else: merged_arr.append(arrB.pop(0))
        elif bool(arrA[0]):
            merged_arr.extend(arrA)
        else: 
            merged_arr.extend(arrB)
 
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) == 1):
        return arr
    
    leftSide = arr[:int((len(arr)-1)/2)]
    rightSide = arr[int((len(arr)-1)/2):]
    leftSide = merge_sort(leftSide)
    rightSide = merge_sort(rightSide)
    arr = merge(leftSide, rightSide)
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
def timsort( arr ):

    return arr
