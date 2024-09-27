class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            dirs = [
                (-1,0),
                (1,0),
                (0,1),
                (0,-1)
            ]
            while q:
                row, col = q.popleft()
                for rm, cm in dirs:
                    r, c = row + rm, col + cm
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == "1" and (r, c) not in visited):
                        
                        visited.add((r, c))
                        q.append((r, c))
                    
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands 
