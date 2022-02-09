# using recursive
def binary_search_recursive(arr,low,high,x):
    if high>=0:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

#using iterative
def binary_search_iterative(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            return mid
    return -1