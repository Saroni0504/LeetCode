'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
x can be 0 or n can be negative
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        elif n < 0:
            return self.myPow(1/x, -n)
        
        if n % 2 == 0:
            temp = self.myPow(x, n/2)
            return temp * temp
        
        else:
            return x * self.myPow(x, n - 1)
