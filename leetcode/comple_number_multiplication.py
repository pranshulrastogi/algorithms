'''
Problem link: https://leetcode.com/problems/complex-number-multiplication/
Difficulty: Medium
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        '''
        Numbers are treated as: num1 = a+bi, num2 = c+di
        '''
        real, img = "",""
        a,b=num1.split('+')
        b = b[:-1] # remove the 'i'
        c,d = num2.split('+')
        d = d[:-1] # remove the 'i'
        a,b,c,d = int(a), int(b), int(c), int(d) # convert all to int
        
        real_int = (a*c - b*d) # calculate the real part
        img_int = (a*d + b*c) # calculate the imaginary part
        real = str(real_int)
        img = str(img_int)
        ans = f"{real}+{img}i"
        return ans