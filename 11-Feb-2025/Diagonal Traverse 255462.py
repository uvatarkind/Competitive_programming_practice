# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        table = defaultdict(list)
        for i in range(n):
            for j in range(m):
                table[i+j].append(mat[i][j])
        lis = sorted(table.items())
        res = []
        for i in range(len(lis)):
            if not i % 2:
                lis[i][1].reverse()
                res.extend(lis[i][1])
            else:
                res.extend(lis[i][1])
        return res