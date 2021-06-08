'''
leetcode link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: Medium
Problem Statement:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        l = len(preorder)
        position = {preorder[i]:inorder.index(preorder[i]) for i in range(l)}
        
        def fix(value, root):
            '''
            fixes/attaches value in the tree with root 'root'
            Algorithm:
            1st element of preorder gives us the root
            after that relative position of the elements in 'inorder Traversal' 
            gives the position of that node in tree
            '''
            if position[root.val] < position[value]:
                if not root.right:
                    root.right = TreeNode(val=value)
                else:
                    fix(value, root.right)
            else:
                if not root.left:
                    root.left = TreeNode(val=value)
                else:
                    fix(value, root.left)
            
            return root
            
        # define 1st value in preorder traversal as root
        root = TreeNode(val=preorder[0])
        # fix all other values in preorder as per there relative position in inorder traversal
        for i in range(1,l):
            root = fix(preorder[i], root) 
        return root
