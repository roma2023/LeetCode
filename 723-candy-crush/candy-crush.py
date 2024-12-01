class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])
        done = True

        # let's not overcomplicate this, we can easily do the flagging part just by 
        # first, crushing through ROWS
        for r in range(rows): 
            for c in range(cols - 2): 
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
                    done = False
        # second, crushing through COLS
        for c in range(cols): 
            for r in range(rows - 2): 
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
                    done = False                

        # third, gravity
        if not done:
            for c in range(cols):
                
                idx = rows - 1
                for r in range(rows-1, -1, -1):
                    # drop the positive values down
                    if board[r][c] > 0: # if not positive
                        board[idx][c] = board[r][c]
                        idx -= 1

                # fill in the rest of cells with 0's
                for i in range(idx, -1, -1):
                    board[i][c] = 0
        print(board)
        return board if done else self.candyCrush(board)

        

