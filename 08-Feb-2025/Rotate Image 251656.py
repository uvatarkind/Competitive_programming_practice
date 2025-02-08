# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        """
        res = [[True] * len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if res[i][j] and res[j][i]:
                    matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
                    res[i][j], res[j][i] = False, False
        for row in matrix:
            row.reverse()
