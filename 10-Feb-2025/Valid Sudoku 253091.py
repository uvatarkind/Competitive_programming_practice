# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue  

                if num in row_sets[i]:
                    return False
                row_sets[i].add(num)

                
                if num in col_sets[j]:
                    return False
                col_sets[j].add(num)

            
                box_index = (i // 3) * 3 + (j // 3)
                if num in box_sets[box_index]:
                    return False
                box_sets[box_index].add(num)

        return True