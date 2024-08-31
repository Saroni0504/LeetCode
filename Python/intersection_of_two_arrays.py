'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection. Each element in the result must be unique and you may return the result in any order.
'''
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1.intersection(nums2)

# one liner solution
class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)
        
