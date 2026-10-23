import math
def calculate_hours(piles, j):
    hours = 0
    for i in range(len(piles)):
        hours = hours + math.ceil(piles[i]/j)
    return hours

def koko_loves_bananas(piles, h):
    max_fruits = float("-inf")
    for i in range(len(piles)):
        if max_fruits < piles[i]:
            max_fruits = piles[i]

    start = 1
    end = max_fruits
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        hours = calculate_hours(piles, mid)
        if hours <= h:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

    '''
    i = 1
    while i < (max_fruits):
        hours = calculate_hours(piles, i)
        if hours <= h:
            return i
        i +=1
    return max_fruits
    '''
piles = [30,11,23,4,20]
h = 5
anss = koko_loves_bananas(piles,h)
print(anss)