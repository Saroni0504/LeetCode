''' Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3. '''

# O(n)
class Solution:
    def containsDuplicate(self, nums):
        hashSet = set() 
        for n in nums: 
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False
