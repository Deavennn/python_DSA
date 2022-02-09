def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

array = [1,5,3,4,2,1,5,6,7,5,4,6,8,5,6,7,8]
print(bubble_sort(array))