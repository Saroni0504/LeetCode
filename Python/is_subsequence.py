'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s, t):
        if s == t or len(s) == 0:
            return True
        idx = 0
        for c in t:
            if s[idx] == c:
                if idx == len(s) - 1:
                    return True
                idx += 1
        return False
