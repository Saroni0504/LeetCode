'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''


#loop solution
class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
           return False
        if n == 1:
            return True
 
        while n > 1:
            if not (n % 4 == 0):
                return False
            n /= 4
        return True
#without loops
class Solution:
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        if n <= 0:
            return False
        
        logarithm_base = math.log(n) / math.log(4)
        
        return (logarithm_base == int(logarithm_base))      
        
