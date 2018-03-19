"""

find the maximum sum over all subarrays of a given array of integer.

-5, -2, 1, 2, 3, 4, -5, -6, -7, -8, 9

Answer is 10 for 1, 2, 3, 4

Assume an array with sums for 0 to i stored in index i

s[0] = -5
s[1] = -7
s[2] = 1
s[3] = 2
s[4] = 3
s[5] = 4

and so on

Maximum sub array will have this property

[0 to some_index] will be a minimum subarray

[some_index + 1 to present_index] will be the maximum sum1


"""

def find_max_of_subarray(nums):
    min_sum = 0
    sum1 = 0
    max_sum = 0
    for i in range(len(nums)):
        sum1 += nums[i]
        if sum1 < min_sum:
            min_sum = sum1
        if (sum1 - min_sum) > max_sum:
            max_sum = sum1 - min_sum
        
    return max_sum



nums = [-5, -2, 1, 2, 3, 4, -7, -4, 3,  -1, 11, -7, -8, 8]
print find_max_of_subarray(nums)
