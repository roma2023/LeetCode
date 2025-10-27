
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1-15 => length for this certainlength in how many ways we can construct a word, 2^mn * 15
        
        ROWS, COLS = len(board), len(board[0])
        visited = set() # (r, c)
        length = len(word)

        def dfs(row, col, i):

            if i == length:
                return True
                
            if row not in range(0, ROWS) or col not in range(0, COLS) or (row, col) in visited or word[i] != board[row][col]:
                return False
            
        
            visited.add((row, col))
            res = (dfs(row+1, col, i+1) or
                    dfs(row, col+1, i+1) or
                    dfs(row-1, col, i+1) or
                    dfs(row, col-1, i+1))
            visited.remove((row, col))
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:  
                    if dfs(row, col, 0):
                        return True

        return False 

