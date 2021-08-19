'''
Problem link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Difficulty: Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def good(root, mx):
            if not root:
                return 0
            elif not root.left and not root.right:
                #leaf 
                if root.val >= mx:
                    return 1
                else:
                    return 0
            else:
                val = root.val
                if val >= mx:
                    mx=val
                    return 1+good(root.left, mx) + good(root.right, mx)
                else:
                    return good(root.left, mx) + good(root.right, mx)
        ans = good(root, -1*(10**4+1))
        return ans
                
        