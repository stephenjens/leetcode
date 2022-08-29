# 08/29/2022 15:44	Accepted	458 ms	16.4 MB	python3

# totally ripped this off from the solutions
# the idea is to find a "1" in the grid, mark that as 0 and then do a dfs on its max of 4 neighbors
def dfs(grid: List[List[str]], i: int, j: int):
    m = len(grid)
    n = len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
        return
    grid[i][j] = "0"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(grid, i, j)
        return num_islands
