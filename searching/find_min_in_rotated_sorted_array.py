"""
Find minimum in minimun sorted array. 

arr = [1,2,3,4]
ans: 0

arr = [3,4,1,2]
ans = 2

approach: take a mid. if mid to end is sorted then update mini, look on the left side

Time Complexity: O(log n)

"""
def min_in_rotated_array(arr):
    mini = float("inf")
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2 
        if arr[mid] <= arr[end]:
            mini = min(mini, mid)
            end = mid - 1
        else:
            start = mid + 1
    return mini

    

arr = [3,4,5,7,1,2]
ans = min_in_rotated_array(arr)
print(arr,ans)

arr = [7,6,1,2,3,4,5]
ans = min_in_rotated_array(arr)
print(arr,ans)



