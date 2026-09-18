class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            found = []

            for j in range(len(board)):
                num = board[i][j]

                if num in found and num != ".":
                    return False
                
                found.append(num)
        
        for i in range(len(board)):
            found = []

            for j in range(len(board)):
                num = board[j][i]

                if num in found and num != ".":
                    return False

                found.append(num)
        

        row_idx = 0
        column_idx = 0

        while column_idx < len(board) - 1:
            while row_idx < len(board) - 1:
                found = []

                for i in range(row_idx, row_idx + 3):    
                    for j in range(column_idx, column_idx + 3):
                        num = board[i][j]

                        if num in found and num != ".":
                            return False

                        found.append(num)

                row_idx += 3
            
            row_idx = 0
            column_idx += 3

        return True




