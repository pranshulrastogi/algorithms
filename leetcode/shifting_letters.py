'''
Problem link:
Difficulty: 
'''
import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = list(string.ascii_lowercase)
        letters_dict = {letters[i]:i for i in range(26)}
        sm = sum(shifts)
        cum_shifts = [sm]
        for i, ele in enumerate(shifts[:-1], start=1):
            cum_shifts.append(cum_shifts[i-1]-ele)
        
        result = ""
        for i, char in enumerate(s):
            # get the index
            idx = letters_dict.get(char)
            idx = (idx+cum_shifts[i])%26
            result += letters[idx]
        return result
            