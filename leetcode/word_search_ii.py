"""
Problem link: https://leetcode.com/problems/word-search-ii/
Difficulty: Hard
"""


def findWords(board, words):
    r_c, c_c = len(board), len(board[0])

    def dfs(r, c, word, l, i, visited):
        if r < 0 or c < 0 or r >= r_c or c >= c_c:
            return False
        if (r, c) in visited:
            return False
        if i >= l:
            return False
        if i == 0:
            return board[r][c] == word[i]
        if i < 0:
            return False

        if board[r][c] != word[i]:
            return False

        visited.add((r, c))
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for row_col in neighbours:
            new_r, new_c = r + row_col[0], c + row_col[1]
            if dfs(new_r, new_c, word, l, i - 1, visited):
                return True
        visited.remove((r, c))
        return False

    ans = []
    for word in words:
        done = False
        for r in range(r_c):
            for c in range(c_c):

                if board[r][c] == word[-1]:
                    l = len(word)
                    if dfs(r, c, word, l, l - 1, set()):
                        ans.append(word)
                        done = True
                        break
            if done:
                break
    return ans
