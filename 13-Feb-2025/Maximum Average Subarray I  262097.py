# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = mx = sum(nums[:k]) 
        for i in range (k , len(nums)):
            curr_sum +=nums[i] - nums[i-k]
            mx = max(mx,curr_sum)
        return mx/k