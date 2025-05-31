# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def merge(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return 
        if self.size[pu] < self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        dsu = DSU(n * m)
        
        def index(i, j):
            return i * m + j

        allowed = ((1, 3, 0), (1, 5, 0), (2, 6, 1), (2, 5, 1), (2, 2, 1), (3, 2, 1), (3, 5, 1), (3, 6, 1), (4, 1, 0), (4, 5, 1), (4, 6, 1), (4, 2, 1), (4, 3, 0), (6, 1, 0), (6, 5, 0), (1, 1, 0))
        
        def merge_nodes(i1, j1, i2, j2, dir):
            if 0 <= i1 < n and 0 <= j1 < m and 0 <= i2 < n and 0 <= j2 < m:
                node1 = index(i1, j1)
                node2 = index(i2, j2)
                if (grid[i1][j1], grid[i2][j2], dir) in allowed:
                    dsu.merge(node1, node2)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    merge_nodes(i, j, i, j + 1, 0)
                    merge_nodes(i, j - 1, i, j, 0)
                elif grid[i][j] == 2:
                    merge_nodes(i, j, i + 1, j, 1)
                    merge_nodes(i - 1, j, i, j, 1)
                elif grid[i][j] == 3:
                    merge_nodes(i, j - 1, i , j, 0)
                    merge_nodes(i, j, i + 1, j, 1)
                elif grid[i][j] == 4:
                    merge_nodes(i, j, i, j + 1, 0)
                    merge_nodes(i, j, i + 1, j, 1)
                elif grid[i][j] == 5:
                    merge_nodes(i - 1, j, i, j, 1)
                    merge_nodes(i, j - 1, i, j, 0)
                elif grid[i][j] == 6:
                    merge_nodes(i, j, i, j + 1, 0)
                    merge_nodes(i - 1, j, i, j, 1)
        return dsu.find(0) == dsu.find(n * m - 1)