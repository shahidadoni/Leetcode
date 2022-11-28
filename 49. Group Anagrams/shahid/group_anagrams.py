from typing import List
# Solution 1 (Brute Force)
# Passing two string to anagram check function if true 
# adding it in list
# This solution exceeds time limit

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Function for checking two functions are anagram
        def isAnagram(s: str, t: str) -> bool:

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

        # Initializing result List
        result = []

        # list for only checking duplicates 
        unique_strings=[]

        # making a copy of input list 
        strs_copy = strs.copy()

        # looping through the original input list
        for str1 in strs:

            # checking whether the string is in unique, if true skip
            if str1 in map:
                continue

            # temporary list for appending it to result list
            temp_list = []

            #adding string to both the list
            temp_list.append(str1)
            map.append(str1)

            # removing string from the input_copy list
            # so we dont iterate and check for anagram for duplicates
            strs_copy.remove(str1)
            
            # looping through input_copy list which has no duplicates 
            for str2 in strs_copy:
                # if str2 in map:
                #     continue

                # checking anagram
                is_anagram = isAnagram(str1,str2)

                # if true adding string to sub list i.e. temp_list
                if is_anagram:
                    temp_list.append(str2)
                    map.append(str2)
            
            # adding temp_lists in result list
            result.append(temp_list)

        return result
        
# Solution 2 (Using Hashmap)

# This solution makes hash for a particular string 
# and checks other string hashes against it in map

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # map for storing hash of strings as key
        # and list of strings which are anagrams as value
        map ={}

        
        for string in strs:

            # list for creating hash of a string
                hash_list = [0] * 26

                # looping letter by letter
                for ch in string:

                    # using ord to get unicode value of character
                    # and subtracting ASCII/unicode value of character 'a' from it.
                    # increment the value as a position in hash list
                    hash_list[ord(ch) - ord('a')] += 1

                # stringifying all elements as hash value
                hash = ''.join([(str(elem) + ',') for elem in hash_list])

                # putting hash as key in map & string in a list as a value
                # and checking if the key is already present
                if hash not in map:
                    map[hash] = [string]
                else:
                    map[hash].append(string)

        #returning values of all keys in map in a list
        return list(map.values()) 