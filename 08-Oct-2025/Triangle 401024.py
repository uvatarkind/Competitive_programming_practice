# Problem: Triangle - https://leetcode.com/problems/triangle/

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        memo = [[0]*m for _ in range(m)]
        
        for i in range(m):
            for j in range(i+1):
                if i == 0 and j == 0:
                    memo[i][j] = triangle[i][j]
                else:
                    num1 = memo[i-1][j-1] if j-1 >= 0 else float('inf')
                    num2 = memo[i-1][j] if j <= i-1 else float('inf')
                    memo[i][j] = triangle[i][j] + min(num1, num2)
        
        return min(memo[m-1]) 
