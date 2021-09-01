'''
Problem link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
Difficulty: medium
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        
        def reorder(stk):
            print(f"got {stk}")
            while len(stk)>2 and stk[-1]=='#' and stk[-2]=='#':
                stk.pop(-1)
                stk.pop(-1)
                if stk[-1] != '#':
                    stk.pop(-1)
                    if stk:
                        stk.append('#')
            
            print(f"returning {stk}")
            return stk
        
        if len(preorder)==1:
            if preorder[-1]=='#':
                return True
            else:
                return False
        stack = []
        lst = preorder.split(',')
        ln = len(lst)
        for i,ele in enumerate(lst):
            if ele != '#':
                stack.append(ele)
            else:
                stack.append('#')
                stack = reorder(stack)
            if i<ln-1 and not stack:
                return False
        if stack:
            return False
        else:
            return True