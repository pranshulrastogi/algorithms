'''
Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: Easy
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def bst(i, j):
            if i>j:
                return None
            else:
                mid = (i+j)//2
                node = TreeNode(nums[mid])
                node.left = bst(i,mid-1)
                node.right = bst(mid+1, j)
                return node
        l = len(nums)
        tree = bst(0, l-1)
        return tree