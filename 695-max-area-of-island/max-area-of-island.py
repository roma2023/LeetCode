class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c): 
            if (r not in range(rows) or c not in range(cols) or 
            grid[r][c] == 0 or grid[r][c] == 2): 
                return 0
            grid[r][c] = 2
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c - 1) + 
                        dfs(r, c + 1)) 
        
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    maxArea = max(maxArea, dfs(r, c)) 
        return maxArea