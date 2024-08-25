'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''
class Solution(object):
    def reverse(self, x):
        negative = False
        if x < 0:
            x *= -1
            negative = True
        x = str(x)
        reverse_x = x[::-1]
        reverse_x = int(reverse_x)
        if negative == True:
            reverse_x *= -1
        if reverse_x > 2**31 - 1 or reverse_x < -2**31 + 1:
            return 0
        else:
            return reverse_x       
