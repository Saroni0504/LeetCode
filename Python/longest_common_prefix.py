'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs or strs[0] == "": 
            return ""
        if len(strs) == 1:
            return strs[0]
        
        first_word = strs[0]
        prefix = ""
        for l in first_word:
            prefix += l
            for s in strs[1:]:
                if not s.startswith(prefix):
                # without using startswith: if s[:len(prefix)] != prefix:
                    return prefix[:-1]
        return prefix
