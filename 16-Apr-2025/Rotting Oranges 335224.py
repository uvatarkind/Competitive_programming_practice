# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        qu = deque()
        fresh = 0
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    qu.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
    
        if fresh == 0:
            return 0
        
        while qu:
            minutes += 1
            for _ in range(len(qu)):
                i, j = qu.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2    
                        fresh -= 1
                        qu.append((ni, nj))
                        
            if fresh == 0:
                return minutes
        
        return -1        