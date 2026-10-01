"""
Ques: Given array is unique and sorted. It might be rotated by k times.
find the target value

arr = [1,2,3,4,5,6,7,8,9]
n = 10
Ans: -1

arr = [1,2,3,4,5,6,7,8,9]
n = 4
Ans: 3

arr = [10,13,15,16,1,3,4,5,7,8]
n = 15
Ans: 2

approach: use binary search and find the mid == target, return mid
now check which part is sorted
if arr[mid] <= arr[end]
2nd part is sorted. check if the target lies in the sorted part if not move to the other part
else
1st part is sorted. check if the target lies in the sorted part if not move to the other part

Time complexity: O(log n)

"""

def search_in_rotated_array(arr,target):
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] == target :
            return mid
        if arr[mid] <= arr[end]:
            if arr[mid] <= target <= arr[end]:
                begin = mid + 1
            else:
                end = mid - 1
        else:
            if arr[begin] <= target <= arr[mid]:
                end = mid - 1
            else:
                begin = mid + 1
    return -1
print("Enter 15 elements")
arr =[]

arr = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
n = 4
"""
for i in range(15):
    arr.append(int(input()))
print("Enter the element your target")
n = int(input())
"""
ans = search_in_rotated_array(arr,n)
print(ans)