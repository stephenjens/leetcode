# 09/10/2022 15:30	Accepted	6373 ms	14 MB	python3
# same as solution.py but stops early instead of checking all 4 neighbors inside any(...)
def search(board: List[List[str]], i: int, j: int, word: str) -> bool:
    if len(word) == 0:
        return True
    m = len(board)
    n = len(board[0])
    
    if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[0]:
        return False
  
    # mark this position
    board[i][j] = '#'
    
    found = False
    # check neighbors
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        found = search(board, i + x, j + y, word[1:])
        if found:
            break
    if not found:
        board[i][j] = word[0]
    
    return found

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if search(board, i, j, word):
                    return True
        return False
