'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
            
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
