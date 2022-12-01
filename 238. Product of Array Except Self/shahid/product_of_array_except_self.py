from typing import List
# This solution calculates value of current position 
# which is product till current position - 1 of original array  in first loop
# from starting index to end index.
# Example: current position = product till (current - 1) position

# Second loop calculate from end index till start index 
# but this time the value of current position is the product of current position of result array
# with product till current position + 1 of original array.
# Example: current position = current position of result array * product till (current + 1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(0,n,1):
            if i > 0:
                left = left * nums[i-1]
            res[i] = left

        right = 1
        for i in range(n-1,-1,-1):
            if i < n - 1:
                right = right * nums[i+1]
            res[i] *= right

        return res
