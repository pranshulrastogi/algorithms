'''
Link: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium
Problem statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
class Solution:
    # its like a binary tree, maximum 2 options
    # maintain stack and string down the line
    # if ) need to be added, stack need to be popped
    # else stack need to be pushed
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def pos(expr, stck, n):
            if not stck and n==0:
                print(expr)
                ans.append(expr)
            else:
                
                if not stck and n>0:
                    # print(expr)
                    pos(expr+'(', stck+['('], n-1)
                elif n==0 and stck:
                    stck.pop()
                    pos(expr+')',stck, n)
                elif n>0 and stck:
                    # 2 options
                    # print(n-1)
                    pos(expr+'(', stck+['('], n-1)
                    stck.pop()
                    pos(expr+')', stck, n)
        pos("", [], n)
        print(ans)
        return ans 