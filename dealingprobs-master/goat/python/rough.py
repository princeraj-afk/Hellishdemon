def binarySearch(arr,low,high,x):
    mid = (high+low)//2
    if x>arr[low] and x<arr[high] and high-low==1:
        return low+1
    elif arr[mid]<x:
        return binarySearch(arr,mid+1,high,x)
    else:
        return binarySearch(arr,low,mid-1,x)


arr = [ 2, 3, 4, 10, 40 ]
x = 10
print(binarySearch(arr,0,4,50))