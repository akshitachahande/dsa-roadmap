"""
Ques: Find the last occurrence of the given number in an array

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 1
Ans: 2

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 30
Ans: -1

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = 7
Ans: 10

approach: use binary search where condition is if arr[mid] == target then
update the result
res = mid
check on the right side if more elements are present or not
start = mid + 1

Time complexity: O(log n)

"""
def last_occurrence(arr, n):
    res = -1
    begin = 0 
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if n == arr[mid]:
            res = mid
            begin = mid + 1
        elif n > arr[mid]:
            begin = mid + 1
        else: 
            end = mid - 1
    return res

print("Enter 5 elements")
arr = []
for i in range(5):
    arr.append(int(input()))
print("Enter the element you want to search")
n = int(input())
ans = last_occurrence(arr,n)
print(ans)