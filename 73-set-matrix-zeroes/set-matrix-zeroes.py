class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        dirs = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        def dfs(r,c, d):
            if r not in range(rows) or c not in range(cols):
                return
            
            if matrix[r][c] == 0:
                matrix[r][c] = "0"
                for row, col in dirs:
                    dfs(r + row, c + col, [row, col])
                return
            
            matrix[r][c] = "0"
            row, col = d[0], d[1]
            print(row,col)
            dfs(r + row, c + col, [row, col])
            return

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    dfs(r,c, dirs)
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    matrix[r][c] = 0

        return matrix