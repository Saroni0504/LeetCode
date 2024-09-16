'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
# using O(1) space O(n) runtime
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            ans = ans ^ nums[i]
        return ans  
# using O(n) space , O(n) runtime
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        res = 0
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i],0) + 1 
        for k, v in counter.items():
            if counter[k] == 1: 
                res += k
        return res
