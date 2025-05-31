# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = []
        
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                dist.append((dis, i, j))
        
        heapq.heapify(dist)

        
        par = [i for i in range(n)]
        msum = 0
        while n > 1:
            d, i, j = heapq.heappop(dist)
            pari, parj = par[i], par[j]
           
            while par[pari] != pari:
                pari = par[pari]
            while par[parj] != parj:
                parj = par[parj]
            
            if pari != parj:
                n -= 1
                par[pari] = parj
                msum += d
        return msum
        