'''
Problem Statement: https://leetcode.com/problems/push-dominoes/
Diffilutly: Medium
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        
        def push(dom):
            padded = "."+dom+"."
            res = ""
            for i, ele in enumerate(padded[1:-1],start=1):
                left = padded[i-1]
                right = padded[i+1]
                if ele=='.':
                    if left == 'R':
                        if right == 'L':
                            out = "."
                        else:
                            out = 'R'
                    elif right == 'L':
                        out = 'L'
                    else:
                        out = "."
                else:
                    out = ele
                res += out
            return res
        
        curr = dominoes
        while True:
            pushed = push(curr)
            if pushed == curr:
                ans = pushed
                break
            else:
                curr=pushed
        print(ans)
        return ans