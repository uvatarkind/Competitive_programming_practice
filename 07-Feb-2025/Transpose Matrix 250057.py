# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        new_matrix = [[0]*row for j in range(col)]

        for i in range(row):
            for j in range(col):
                new_matrix[j][i]=matrix[i][j]
        return new_matrix