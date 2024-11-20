class Solution(object):
    def removeElement(self, nums, val):
        k = 0 
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: 
                k += 1
                i += 1
        return k
