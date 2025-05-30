from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):

            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r,c) in visited ): 
                return 
            
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == '1' and (r,c) not in visited: 
                    islands += 1
                    dfs(r,c)
        return islands
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

obj = Solution()
print(obj.numIslands(grid))  # Output: 3

# you can just directly also do dfs[r][c] = 0 as well but it modifies input 
