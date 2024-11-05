# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#                 # The number of unique paths can be seen as the number of ways to choose m−1 downs and n−1 rights, regardless of the order. In combinatorial terms. 
            
#             ways_to_choose_n_1 = math.comb(m+n-2, n-1)
            
#             return ways_to_choose_n_1
        # math solution
        # [[][][]].  # all the outer layers came through 1 path only, and max they are part of m-1 + n-1 paths, the inner layers could have been discovered through 2 different ways, either coming from up or from the left, 
        # 7 x 3 => 28    2 x 2 => 2.   2 x 3 => 3   (1 + 2) 
        # [[][][]]



        # OBS: every time we make right or down move, we decrease either m or n by 1 and create a new subproblem
        # Q: how many different such subproblems exist (mn)

        
        # [[][][][]]
        # [[][][][]]
        # [[][][][]]

# DP more space optimal solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1] * n
        print(row)

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1): 
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]

# DP solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0 for i in range(n)] for j in range(m)]
        print(grid)

        grid[m-1][n-1] = 1

        for i in range(m-1, -1,-1):
            for j in range(n-1, -1, -1): 
                if i < m - 1 and j == n - 1:
                    grid[i][j] += grid[i+1][j]
                elif i == m - 1 and j < n -1: 
                    grid[i][j] += grid[i][j+1]
                elif i < m - 1 and j < n -1: 
                    grid[i][j] += grid[i+1][j] + grid[i][j+1]
        
        return grid[0][0]
                     
                    