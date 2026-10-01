# Traverse through each element to find the element
# Time complexity: O(n)

def linear_search(arr,n):
    for i in range(5):
        if arr[i] == n:
            return i

print("Enter 5 elements")
arr = []
for i in range(5):
    arr.append(int(input()))
print("Enter the element you want to search")
n = int(input())
ans = linear_search(arr,n)
print(ans)

