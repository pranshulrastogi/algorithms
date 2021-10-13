"""
Problem link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Difficulty: Medium
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstFromPreorder(preorder):
    def find_pos(node, root):
        if not root:
            return None
        if not root.left and not root.right:
            return (0, root) if node.val >= root.val else (-1, root)
        if node.val >= root.val:
            return find_pos(node, root.right) if root.right else (0, root)
        else:
            return find_pos(node, root.left) if root.left else (-1, root)

    root = TreeNode(preorder[0])
    for val in preorder[1:]:
        # create node
        node = TreeNode(val)
        # find node's position
        pos, parent = find_pos(node, root)
        if pos < 0:
            parent.left = node
        else:
            parent.right = node
    return root
