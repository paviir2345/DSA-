def count_occurence(arr,target):
    first = -1
    last = -1

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
       
             right = mid - 1

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] ==target:
             last = mid 
             left = mid + 1
        elif arr[mid] < target:
             left = mid + 1
        else :
              right = mid - 1
    if first == -1:
        return 0
    return last - first + 1

arr = [1,1,2,2,2,2,3]
target = 2
print(count_occurence(arr,target))
      
      


