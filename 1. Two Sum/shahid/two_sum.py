from typing import List
# Solution 1 (Brute Force)
    # exceeds time limit
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Looping through the array and initializing i at zeroth index
        for i in range(len(nums)-1):

            # Looping again but this time initializing j at i+1 index
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]

                # checking if sum is equals to target
                if sum == target:
                    return [i,j]

        return []

# Solution 2 (Using Hashmap)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Creating Hashmap to store value as key and its index as value
        map = {}

        # Storing array value and its index in map
        for i in range(len(nums)):
            map[nums[i]] =  i
        
        # Looping and checking map for the remainder of current value subtracted from target
        for i in range(len(nums)):
            val = nums[i]
            rem = target - val

            # Getting index of the value
            if rem in map:

                # Making sure current index in not equal to index in map
                if i==map[rem]:
                    continue

                # returning current index and index of remainder value from the map
                return [i,map[rem]]

        # returning empty list if above conditions not satisfied
        return []