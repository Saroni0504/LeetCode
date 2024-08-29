'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            h = min(height[left],height[right])
            w = right - left
            current_area = h*w
            max_area = max(max_area,current_area)
            if h == height[left]:
                left += 1
            else:
                right -= 1
        return max_area 

    
        
        
