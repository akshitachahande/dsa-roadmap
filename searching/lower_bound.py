"""
Ques: Find the lower bound of the given array

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 1
Ans: 0

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 7
Ans: 8

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 0
Ans: 15

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 4
Ans: 6

approach: use binary search where condition is if arr[mid] >=  target then lb = mid

Time complexity: O(log n)

"""

def lower_bound(arr, target):
    lb = len(arr)
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] >= target:
            lb = mid
            end = mid - 1
        else:
            begin = mid + 1
    return lb

print("Enter 15 elements")
arr =[]
"""
arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 12
"""
for i in range(15):
    arr.append(int(input()))
print("Enter the element your target")
n = int(input())

ans = lower_bound(arr,n)
print(ans)
