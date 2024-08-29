'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        s = set()
        # we get the first value fixed each iteration and because we need
        # triplets of values we loop until the length - 2
        for i in range(len(nums)-2):
            j = i + 1 
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    s.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return s
            
        # this approach exceeds runtime at some cases, not good 
        # s = set()
        # h = {value: index for index, value in enumerate(nums)}
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         third_num = -nums[i] - nums[j]
        #         if third_num in h and h[third_num] != i and h[third_num] != j:
        #             s.add(tuple(sorted([nums[i],nums[j],third_num]))) 
        # return s
        

        

        
