'''
Given an integer, convert it to a Roman numeral.
constraints- number between 1 to 3999
'''
class Solution:
    def intToRoman(self, num):
        romans = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),
        (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        i = 0
        roman_number = ''
        while num != 0:
            if num - romans[i][0] >= 0:
                roman_number += romans[i][1]
                num -= romans[i][0]
            else: 
                i += 1
        return roman_number
                
