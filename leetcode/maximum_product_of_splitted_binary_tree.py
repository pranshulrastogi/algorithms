'''
Problem link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
Difficutly: Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def get_sum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            return get_sum(root.left) + get_sum(root.right)+root.val
        
        sm = get_sum(root) # get the sum of full tree
        possible_ans = [] # products at every node except leaf nodes
        def mp(root):
            if not root: return 0
            if not root.left and not root.right: return root.val
            l= mp(root.left) # get the sum of the left subtree
            r = mp(root.right) # get the sum of the right subtree
            temp = max((sm-r)*r, (l*(sm-l))) # check if removing left gives you bigger answer or right
            possible_ans.append(temp) # append to possible list
            return l+r+root.val # return the sum for parent
        mp(root)
        ans = max(possible_ans) % (10**9+7)
        return ans
        