'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_arr = self.count_occ(ransomNote)
        magazine_arr = self.count_occ(magazine)
        for c in ransomNote:
            # if a character in ransom note appears more times than in magazine
            # it means that we can't construct the ransomNote from Magazine
            if ransom_arr[ord(c) - ord('a')] > magazine_arr[ord(c) - ord('a')]:
                return False
        return True
    #count occurances in a string of all alphabet letters 
    def count_occ(self,s):
        chars = [0]*26
        for c in s:
            chars[ord(c) - ord('a')] += 1
        return chars

#Dictionary solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dictionary = {}
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        return True
