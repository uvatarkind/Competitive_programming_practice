# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxheap=[]
        row=len(grid)
        col= len(grid[0])
        max_sum=0

        for i in range(row):
            row_heap=[-val for val in grid[i]]
            heapq.heapify(row_heap)
        
            for _ in range(limits[i]):
                val= -heapq.heappop(row_heap)
                heapq.heappush(maxheap,val)
                max_sum+=val
        while len(maxheap)>k:
            max_sum-=heapq.heappop(maxheap)
        return max_sum