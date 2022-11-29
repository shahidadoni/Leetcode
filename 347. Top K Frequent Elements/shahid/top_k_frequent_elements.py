import collections
import heapq
from typing import List 


# Solution 1 (Using HaspMap Only)
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            
        # if length of list is 1 return the same list
        if len(nums) == 1:
            return nums
        
        # Initialize result List
        result = []
        
        # Hashmap for storing number as key and its frequency as value
        frequency = {}

        # Looping through the input list and storing 
        # number as key and increment the frequency as value 
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            else:
                frequency[num] +=1

        # Looping till i is less than k
        i = 0
        while i<k:

            # Getting List of all values in frequency map and list of keys
            values = list(frequency.values())
            keys = list(frequency.keys())

            # Getting max from values list and getting the index of the max value from values_list
            max_value = max(values)
            max_index = values.index(max_value)

            # Putting the same index and getting the number from keys_list
            num = keys[max_index]

            # Adding to result list and removing from map
            result.append(num)
            frequency.pop(num)
            i +=1

        return result

# Solution2 (Using Hashmap + heapq.nlargest)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Creating Hashmap (using collection.Counter) of key as numbers and value as its frequency
        map = collections.Counter(nums)

        # Initializing list as heap
        heap = []

        # Looping for keys
        for i in map.keys():

            # Pushing value in heap list as a tuple of frequency of number and number itself
            heapq.heappush(heap, (map[i], i))

        # Getting the k numbers with largest frequency
        # Heap sorts the first values of tuple in min to max order
        # if same number it compares the second values
        # That is why we are storing the frequency of number as first value
        # in tuple and pushing into the heap 
        k_largest = heapq.nlargest(k,heap)

        # Initializing result list
        ans = []

        # Looping over the k_largest List and appending the second value of tuple
        # which is the number and not its frequency
        for i, j in k_largest:
            ans.append(j)
            
        return ans

