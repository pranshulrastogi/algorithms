'''
Problem link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
Difficulty: Medium
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedList
        flatten = SortedList()
        for r in matrix:
            for c in r:
                flatten.add(c)
        return flatten[k-1]
