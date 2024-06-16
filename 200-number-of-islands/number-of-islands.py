class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        solved using graphs, we can treat the given as the adjacency matrix representation of the graph, hence we could just do dfs or bfs on it.

        So, we want to iterate through the matrix and pinpoint the visited areas as well as group those adjacent visited cells as one island, so that if we see a completely new unvisited cell we just add 1 to our number of islands and and do bfs or dfs on the that cell pinpointing all the cells that are part of that island as visited , this way when we visit them again, we will not consider them as a separate island. Right!!!

        Let's code it up
        """
        if not grid: return 0

        visited = set() # (row, col)
        numIslands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c): 
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            dirs = [
                [1,0],
                [0,-1],
                [0, 1],
                [-1, 0]
            ]

            while q: 
                row, col = q.popleft()
                for dr, dc in dirs: 
                    r,c = row + dr, col + dc
                    
                    if (r in range(rows) and c in range(cols)
                        and grid[r][c] == "1" and (r,c) not in visited): 

                        visited.add((r,c))
                        q.append((r,c))

                    
        for r in range(rows): 
            for c in range(cols): 

                if grid[r][c] == "1" and (r,c) not in visited: 
                    bfs(r,c)
                    numIslands += 1 
        return numIslands



