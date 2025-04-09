# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols= len(grid), len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        def inbound(row, col):
            return (0 <= row < rows and 0 <= col < cols)
        def dfs(row, col):
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if (inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]=='1'):
                    dfs(new_row, new_col)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
