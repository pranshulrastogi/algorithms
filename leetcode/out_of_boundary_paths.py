'''
Problem LInk: https://leetcode.com/problems/out-of-boundary-paths/
Difficulty: Medium
Problem statement:
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 109 + 7.
Ex:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mem = {} # for saving the state
        def counter(r, c, ml, count):
            if ml < 0: # you can't move so better return 
                return count
            if r < 0 or c < 0 or r >= m or c >= n: # ball is out of the grid, so either count or return
                if ml >= 0:
                    count+=1
                return count
            else:
                if mem.get((r,c, ml), None) is None:
                    
                    # ball can be kicked in 4 directions, so count all the times that it went out for all the four directions
                    mem[(r,c,ml)] = counter(r+1,c,ml-1, count) + counter(r-1, c, ml-1, count) + \
                        counter(r, c+1, ml-1, count) + counter(r, c-1, ml-1, count)
                return mem[(r,c,ml)]%(10**9+7)
        moves_left = maxMove
        ans = counter(startRow, startColumn, moves_left, 0)
        print(ans)
        return ans 
        