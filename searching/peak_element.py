"""
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.

arr = [0,1,0]
output : 1

arr = [0,2,1,0]
output : 1

arr = []

approach: to find the peak compare mid and mid + 1. if mid is smaller move to the right
if mid is greater then peak is to the left that's why end = mid

"""

def peak_element(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start

print("Enter 15 elements")
arr =[]

arr = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]

ans = peak_element(arr)
print(ans)