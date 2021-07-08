'''
Problem link: https://leetcode.com/problems/goat-latin/
Difficulty level: Easy
'''
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u','A','E','O','I','U']
        ans = ""
        
        for i,word in enumerate(sentence.split(),start=1):
            if word[0] in vowels:
                # add ma at last
                postfix = "ma" + 'a'*i
                ans += f" {word}{postfix}"
            else:
                postfix = word[0] + "ma" + 'a'*i
                new_word = word[1:]+postfix if len(word) > 1 else postfix
                ans += f" {new_word}"
       
        return ans.strip()