# Solution 1 (Naive Approach)

    # Iterating through 1st string and 2nd string inside first loop
    # making position of character from 1st string as 0 in 2nd string
    # Doing this till we find no matching character in 2nd string and returning false
    # else true

# Solution 2 (Sorting Approach)
    # Sorting the strings and checking if they are sameclass Solution:
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking length of string and returning false if not same
        if len(s) != len(t):
            return False
        
        # using in-built sorted method and checking if both the string are same
        # after sorting
        return sorted(s)==sorted(t)

#  Solution 3 (Using Dict as hashmap or address table)
    # This solution works for follow up question 
    # i.e. non-english letters or symbols

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:

        # checking length of string and returning false if not same
        if len(s) != len(t):
            return False

        # creating hashmap
        map = {}

        # Looping through first string letter by letter
        for letter in s:

            # checking letter in map if does not exists adding and initializing value to 1
            # if exists incrementing value by 1
            if letter not in map:
                map[letter] = 1
            else:
                map[letter]+=1

        # Looping through 2nd string letter by letter
        for letter in t:    

            # returning false if letter is not in map
            if letter not in map:
                return False
            else:
                # decrementing value by one if exists
                map[letter]-=1
        
        # checking value of each letter key and returning false if not zero
        for value in map.values():
            if value != 0:
                return False

        # returning true atlast i.e. strings are anagram
        return True