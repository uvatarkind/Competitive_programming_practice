# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while top < bottom and left < right:
            #from left to right
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            
            # from top to bottom
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1
            
            if top < bottom:
                # from right to left
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][i])
                bottom -= 1
            
            if left < right:
                # from bottom to top
                for i in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans
