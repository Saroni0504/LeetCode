'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
'''


class Solution(object):
    def findClosestNumber(self, nums):
        closest = float("inf")
        wanted = 0
        for num in nums:
            dist = abs(0 - num)
            if dist < closest:
                closest = dist
                wanted = num
            elif dist == closest:
                if num > wanted:
                    wanted = num 
        return wanted
