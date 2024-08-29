'''
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
'''
from collections import Counter
class Solution:
    def originalDigits(self, s):
        result = ''
        s = s.lower()
        # 0,2,4,6 and 8 have unique characters
        zero = s.count('z')
        two = s.count('w')
        four = s.count('u')
        six = s.count('x')
        eight = s.count('g')
        # After counting the uniques, we can use them to calculate the rest
        one = s.count('o') - zero - two - four
        three = s.count('h') - eight
        five = s.count('f') - four
        seven = s.count('s') - six
        nine = s.count('i') - six - eight - five
        # now I create a dictionary that has the existing digits with the number of 
        # occurances in the string, in an ascending order.
        occurances = {'0': zero, '1': one, '2': two, '3': three, '4': four,
        '5': five, '6': six, '7': seven, '8': eight, '9': nine }
        # now we can concatenate the digits with the number of times they appear
        for key, value in occurances.items():
            if value > 0:
                result += (key*value)
        return result
        
        
