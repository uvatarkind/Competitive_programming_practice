# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def bound(row,col):
            return 0<= row <m and 0<= col < n

        memo=defaultdict(int)

        def dp(row,col):

            down = right =0

            #base case
            if row== m-1 and col== n-1:
                return 1

            if (row,col) in memo:
                return memo[(row, col)]

            if bound(row,col+1):
                down=  dp(row,col+1)

            if bound(row + 1,col):
                right=dp(row+1,col)
            
            memo[(row,col)]= down+right

            return down+right
        
        return dp(0,0)



                
            