 def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Key (r/3, c/3)

        #defaultdict acts like a dictionary except that it doesn't raise an key error.
        # as it produces a key for non-existent value

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True