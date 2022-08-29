# this failed a really big example as it ran out of time :(
def find_one(grid: List[List[str]], seen=[set()]) -> List[int]:
    m = len(grid)
    n = len(grid[0])

    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == "1" and all([(i,j) not in x for x in seen]):
                return (i,j)
    return None
    

def find_neighbors(grid: List[List[str]], x: int, y: int):
    m = len(grid)
    n = len(grid[0])
    neighbors = filter(
        lambda pos: pos[0] >=0 and pos[0] < m and pos[1] >= 0 and pos[1] < n,
        [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    return neighbors
    
    

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # make a graph
        m = len(grid)
        n = len(grid[0])
        
        islands = []
        start = find_one(grid)
        while start != None:
            island = set()
            search = [start]
            while len(search) > 0:
                current = search.pop()
                island.add(current)
                
                for neighbor in find_neighbors(grid, current[0], current[1]):
                    if neighbor not in island and grid[neighbor[0]][neighbor[1]] == "1":
                        search.append(neighbor)
            islands.append(island)
            start = find_one(grid, islands)
        return len(islands)
