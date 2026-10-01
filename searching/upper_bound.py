"""
Ques: Find the upper bound of the given array

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 9
Ans: 12

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 30
Ans: 15

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 0
Ans: 15

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 4
Ans: 6

approach: use binary search where condition is if arr[mid] > target then ub = mid

Time complexity: O(log n)

"""

def upper_bound(arr, target):
    ub = len(arr)
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] > target:
            ub = mid
            end = mid - 1
        else:
            begin = mid + 1
    return ub

print("Enter 15 elements")
arr =[]

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 9
"""
for i in range(15):
    arr.append(int(input()))
print("Enter the element your target")
n = int(input())
"""
ans = upper_bound(arr,n)
print(ans)