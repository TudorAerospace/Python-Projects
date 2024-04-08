#Kadane's Algorithm 2

v = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 7]

def kadane(v):
    curr_sum, max_sum = 0, 0
    for i in range(0, len(v)):
        if curr_sum < 0 or curr_sum + v[i] < 0:
            curr_sum = v[i]
        elif curr_sum + v[i] > 0:
            print(f"Added {v[i]} to {curr_sum}")
            curr_sum += v[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

print(kadane(v))