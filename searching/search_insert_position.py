"""
Ques: Given array with distinctive integers, return index if target is present. else return the insert position
arr = [1,3,5,6]
n = 5
Ans: 2

arr = [1,3,5,6]
n = 2
Ans: 1

arr = [1,3,5,6]
n = 7
Ans: 4

approach: use binary search where condition is if arr[mid] >= target then update pos. else shorten the array of search.
Lower bound logic

Time complexity: O(log n)

"""

def search_insert_position(arr,target):
    pos = len(arr)
    begin = 0
    end = len(arr) - 1

    while(begin <= end):
        mid = (begin + end) // 2
        if arr[mid] >= target:
            pos = mid
            end = mid - 1
        else:
            begin = mid + 1
    return pos



print("Enter 15 elements")
arr =[]

arr = [1,3,4,5,6,7,9,12,13]
n = 30
"""
for i in range(15):
    arr.append(int(input()))
print("Enter the element your target")
n = int(input())
"""
ans = search_insert_position(arr,n)
print(ans)