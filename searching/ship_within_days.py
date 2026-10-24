import math
def cal_days(weights, days):
    day = 0
    i = days
    for j in range(len(weights)):
        if (i - weights[j]) < 0:
            day += 1
            i = days - weights[j]
        else:
            i = i - weights[j]

    return day+1

def ship_within_days(weights, days):
    max_array = max(weights)
    end = sum(weights)
    start = max_array
    final_ans = -1
    print()
    while start <= end:
        mid = (start + end) // 2
        ans = cal_days(weights, mid)

        if mid == max_array and ans < days:
            return mid
        elif ans <= days:
            final_ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return final_ans

'''
brute force approach
def ship_within_days(weights, days):
    max_array = max(weights)
    total_sum = sum(weights)
    i = max_array
    print()
    while i <= total_sum:
        ans = cal_days(weights, i)
        if i == max_array and ans < days:
            return i
        elif ans == days:
            return i
        i += 1
'''

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
output = ship_within_days(weights, days)
print(output)

weights = [3,2,2,4,1,4]
days = 3
output = ship_within_days(weights, days)
print(output)

weights = [1,2,3,1,1]
days = 4
output = ship_within_days(weights, days)
print(output)