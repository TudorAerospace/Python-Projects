#Max Product Subarray 

def max_product(v):
    curr_sum = max_sum = v[0]
    for i in range(1, len(v)):
        if v[i] == 0:
            curr_sum = 1
            pass
        else:
            curr_sum *= v[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum

v = [2, 3, -2, 4, -1, 0, 0, 5, -7, 2, -6, 0]
print(max_product(v))