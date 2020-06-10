def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = arr[0]
        less = [i for i in arr[1:] if i <= p]
        high = [i for i in arr[1:] if i > p]
        return quickSort(less) + [p] + quickSort(high)
    

print(quickSort([3,2,9,6,4]))
