"""
Ques: Given array with integers, return index floor and ceil as the index if target present. else return the nearby positions which are present
arr = [1,3,5,6]
n = 4
Ans: [3,5]

arr = [1,3,5,6]
n = 3
Ans: [3,3]

arr = [1,3,5,8]
n = 6
Ans: [5,8]

approach: use binary search. if target is found return [arr[mid], arr[mid]], if arr[mid] is greater than target, update ceil or else update floor

Time complexity: O(log n)

"""


def floor_the_ceil(arr, target):
    floor = -1
    ceil = -1
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] == target:
            return [arr[mid],arr[mid]]
        elif arr[mid] > target:
            ceil = arr[mid]
            end = mid - 1
        else:
            floor = arr[mid]
            begin = mid + 1
    return [floor,ceil]


print("Enter 15 elements")
arr =[]

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 8
"""
for i in range(15):
    arr.append(int(input()))
print("Enter the element your target")
n = int(input())
"""
ans = floor_the_ceil(arr,n)
print(ans)