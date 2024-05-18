
class Solution:
    def check_for_repetition(self, List: list) -> bool:
        Set = set(List)
        return len(List) == len(Set)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        So, just to clarify thew zie of the sudoku is strictly 9by9 right?
        Hmmm, well as in the given we could go over the eahc row and check if all numbers 1 to 9 are present, meaning there should be no repetitions, we could do the same going over each column and each 3 by 3 block. The brute-force solutiion would take 2 * n* m work to over the columns and rows using nested loops and similarly checking 3by3 blocks also take nm work, which in total result in O(nm) complexity. Right? 

        This is pretty good for the brute force solution and let's try to implement it, how would we check if there are no repetitions, I can think of taking a set of them and checking if the length of the set equal the length of the list, as we know the set will eleiminate all the dupliates, if there is any repetition then their lengths wouldn't be equal right? we could do that but when checking the columns and 3by3 blocks we would need to create a new lists of size 9, which I think is fine. Especially, now I ewalize that we are working with 9by9 matrix, the work should be quite constant. Yes, let's try that
        """

        # checking cols and rows
        for i in range(9): 
            row_list = []
            col_list = []
            for j in range(9): # can be treated as an index of a row or a col
                if board[j][i] != ".":
                    col_list += board[j][i]
                
                if board[i][j] != ".":
                    row_list += board[i][j]

            if not self.check_for_repetition(col_list) or not self.check_for_repetition(row_list):
                return False
            
        # checking 3x3 blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block_list = []
                for m in range(3):
                    for n in range(3): 
                        if board[i+m][j+n] != ".":
                            block_list += board[i+m][j+n]
                
                if not self.check_for_repetition(block_list):
                    return False
        
        return True
            
            