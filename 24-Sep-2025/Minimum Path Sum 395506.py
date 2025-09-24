# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        direction=[(0,1),(1,0)]

        def bound(row ,col):
            return 0<= row< len(grid) and 0<= col<len(grid[0])
        memo= defaultdict(int)
        
        def sol(row,col):
            down=right= float('inf')
            #base case
            if row==len(grid)-1 and col==len(grid[0])-1:
                return grid[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            curr= grid[row][col]
            
            if bound(row+1,col):
                down= curr + sol(row+1,col)
            if bound(row,col+1):
                right = curr + sol(row,col+1)
            
            res= min(down,right)
            memo[(row,col)] = res
            return res

        return sol(0,0)

            
            



        
            


        