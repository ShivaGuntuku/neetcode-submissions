class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sub_grid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c  in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                
                if char in row_sets[r]:
                    return False
                if char in col_sets[c]:
                    return False
                if char in sub_grid_sets[r//3][c//3]:
                    return False
                
                row_sets[r].add(char)
                col_sets[c].add(char)
                sub_grid_sets[r//3][c//3].add(char)
        return True
        