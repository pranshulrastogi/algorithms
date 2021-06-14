'''
leetcode link:https://leetcode.com/problems/smallest-string-starting-from-leaf/
Level: Medium
Problem statement:
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)



'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        strings = [] # to capture all the strings, length will be equal to # of leaf nodes
        def minstr(root, s):
            if not root.left and not root.right:
                # if leaf, add the processed string from leaf to root to strings
                curr = chr(ord('a')+root.val)
                strings.append(curr+s)
            else:
                curr = chr(ord('a')+root.val)
                # make a string
                if root.left:
                    # if root.left exist, that means we haven't reached the string's end
                    minstr(root.left, curr+s)

                if root.right:
                    # if root.right, that means we haven't reached the string's end
                    minstr(root.right, curr+s)
        
        # handle the null case
        if not root:
            return ""
        # populate the strings list
        minstr(root,"")
        
        # sort the string
        strings.sort()
        ans = strings[0]
        return ans