# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operation=0
        while len(nums)>=2 and nums[0]<k:
            x= heapq.heappop(nums)
            y= heapq.heappop(nums)
            z= x*2+y
            heapq.heappush(nums,z)
            operation+=1
        return operation

            
