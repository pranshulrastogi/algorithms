'''
Problem link: https://leetcode.com/problems/decode-ways/
Difficulty: Medium
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        
        def verify(st):
            l = len(st)
            if l <1:
                return 0
            if '0' in st:
                if st[0] == '0':
                    return 0
                else:
                    if int(st) <=26:
                        return 1
                    else:
                        return 0
            n = int(st)
            if l==1:
                if n > 0 and n <=26:
                    return 1
                else:
                    return 0
            elif l==2:
                if n > 0 and n<=26:
                    return 2
                else:
                    return 1
        
        dp = {}
        def decode(i):
            if s[i]=='0':
                return 0
            if len(s[i:]) <=2:
                return verify(s[i:])
            ans = 0
            if not dp.get(i,0):
                for j in range(1,3):
                    if int(s[i:i+j]) <= 26 and int(s[i:i+j]) > 0:
                        ans += decode(i+j)
                dp[i] = ans
                
                    
            return dp[i]
        ans = decode(0)
        print(ans)
        return ans 

            
        