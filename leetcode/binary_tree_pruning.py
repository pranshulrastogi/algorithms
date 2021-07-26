'''
Problem link: https://leetcode.com/problems/binary-tree-pruning/
Difficulty: Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
       
        def pruned(root):
            if not root: return root
            else:
                if not root.left and not root.right:
                    if not root.val==1:
                        return None
                    else:
                        return root
                else:
                    left_subtree = pruned(root.left) # prune the left subtree
                    right_subtree = pruned(root.right) # prune the right subtree
                    root.left = left_subtree
                    root.right = right_subtree
                    if not root.left and not root.right:
                        if not root.val == 1:
                            return None
                        else:
                            return root
                    else:
                        return root
        t = pruned(root)
        return t