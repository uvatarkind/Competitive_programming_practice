# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {-1: -1}
        prefix_sum = 0
        ans = 0
        for i, x in enumerate(nums):
            prefix_sum += x
            val = i - 2 * prefix_sum
            if val in seen:
                ans = max(ans, i - seen[val])
            else:
                seen[val] = i
        
        return ans