# 09/10/2022 15:26	Accepted	9188 ms	13.9 MB	python3
# sort of a dfs, but with backtracking
def search(board: List[List[str]], i: int, j: int, word: str) -> bool:
    if len(word) == 0:
        return True
    m = len(board)
    n = len(board[0])
    
    if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[0]:
        return False
    
    # mark this position
    board[i][j] = '#'
    
    # check neighbors
    if any([
        search(board, i - 1, j, word[1:]),
        search(board, i + 1, j, word[1:]),
        search(board, i, j - 1, word[1:]),
        search(board, i, j + 1, word[1:])
    ]):
        return True
    else: # backtrack
        board[i][j] = word[0]
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if search(board, i, j, word):
                    return True
        return False
