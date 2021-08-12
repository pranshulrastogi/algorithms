'''
Problem link: https://leetcode.com/problems/path-sum-ii/
Difficulty: Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def path(root, c_sum, c_list):
            if not root.left and not root.right:
                # leaf node
                c_sum += root.val
                c_list.append(root.val)
                if c_sum == targetSum:
                    ans.append(c_list)
            else:
                if root.left:
                    path(root.left, c_sum+root.val, c_list+[root.val])
                if root.right:
                    path(root.right, c_sum+root.val, c_list+[root.val])
        path(root, 0, [])
        print(ans)
        return ans