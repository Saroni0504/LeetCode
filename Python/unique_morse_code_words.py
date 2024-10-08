'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
'''

class Solution:
    def uniqueMorseRepresentations(self, words):
        transformations = set()
        for w in words:
            transformations.add(self.convert_to_morse(w))
        return len(transformations)

    def convert_to_morse(self,s):
        s = s.lower()
        morse = ""
        morse_letters = {'a': ".-",'b': "-...",'c': "-.-.",'d': "-..",'e': ".",'f': "..-.",'g': "--.",
        'h': "....",'i': "..",'j': ".---",'k': "-.-",'l': ".-..",'m': "--",'n': "-.",'o': "---",
        'p': ".--.",'q': "--.-",'r': ".-.",'s': "...",'t': "-",'u': "..-",'v': "...-",
        'w': ".--",'x': "-..-",'y': "-.--",'z': "--.."}
        for c in s:
            morse += morse_letters[c]
        return morse

        
