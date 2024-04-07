#Kadane's Algorithm

v = [-2, -3, 4, -1, -2, 1, 5, -3]

def kadane(v):
    curr_sum = max_sum = v[0]
    for i in range(0, len(v)):
        if curr_sum + v[i] > 0 and curr_sum < 0:
            curr_sum = v[i]
        elif curr_sum + v[i] > 0:
            curr_sum += v[i]
        elif curr_sum + v[i] < 0:
            curr_sum = v[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
    print(max_sum)

print(kadane(v))
