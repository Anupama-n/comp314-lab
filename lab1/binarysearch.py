def search(arr,x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left+ (right -left)//2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            right = mid -1

        else:
            left = mid+1
    return -1