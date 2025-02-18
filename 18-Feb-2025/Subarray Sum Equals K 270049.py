# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preSum = defaultdict(int)   
        prefix = 0

        for num in nums:
            prefix += num
            if prefix == k:
                res += 1
            if prefix - k in preSum:
                res += preSum[prefix - k]
            preSum[prefix] += 1

        return res