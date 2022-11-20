from typing import List
# Solution 1 (Naive Approach)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force two pointer using two loops
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        
        return False

# Solution 2 (Intermediate Approach)
class Solution2:
    # Using sort method
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False

# Solution 3 (best approach)
class Solution3: 
    # Using Hashset  
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:return True
            hashset.add(n)
        return False