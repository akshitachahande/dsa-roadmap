#list must be in the sorted order
#Find the target n using binary search
# Approach: Divide and conquer: Find mid, discard the elements which are irrelevant to find the target
# Time Complexity: O(log n)

def binary_search(arr, n):
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end)//2

        if n == arr[mid]:
            return mid
        elif n > arr[mid]:
            begin = mid + 1
        else:
            end = mid - 1

    return -1

print("Enter 5 elements")
arr = []
for i in range(5):
    arr.append(int(input()))
print("Enter the element you want to search")
n = int(input())
ans = binary_search(arr,n)
print(ans)
