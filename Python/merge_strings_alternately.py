'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0 
        j = 0
        isfirstw = True
        result = ""
        while i < len(word1) or j < len(word2):
            if not i < len(word1): 
                result += word2[j]
                j += 1
            elif not j < len(word2):
                result += word1[i]
                i += 1
            else: 
                if isfirstw == True: 
                    result += word1[i]
                    i += 1
                    isfirstw = False
                    continue
                else: 
                    result += word2[j]
                    j += 1
                    isfirstw = True
                    continue
        return result
