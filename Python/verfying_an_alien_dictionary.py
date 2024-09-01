'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
'''
class Solution:
    def isAlienSorted(self,words,order):
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        return False
                    break
        return True
