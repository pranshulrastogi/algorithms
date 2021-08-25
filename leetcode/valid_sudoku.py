'''
Problem Statement: https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(r):
            row = [ele for ele in board[r] if ele!='.']
            l_before = len(row)
            l_after = len(set(row))
            return l_before==l_after
        
        def checkCol(c):
            col = []
            for i in range(9):
                if board[i][c] != '.':
                    col.append(board[i][c])
                    
            l_before = len(col)
            l_after = len(set(col))
            return l_before==l_after
        
        def checkBoxes():
            for i in range(3):
                for j in range(3):
                    box = []
                    for x in range(3):
                        r = 2**i + i + x if i!=0 else 0+x
                        for y in range(3):
                            c = 2**j +j+ y if j!= 0 else 0+y
                            if board[r][c] != '.':
                                box.append(board[r][c])
                    l_before = len(box)
                    l_after = len(set(box))
                   
                    if l_before != l_after:
                        # print("above box failure")
                        return False
            return True
        ans = True
        for r in range(9):
            if not checkRow(r):
                ans=False
                break
        if ans:
            for c in range(9):
                if not checkCol(c):
                    ans = False
                    break
        if ans and not checkBoxes():
            ans=False
        print(ans)
        return ans
                
        