# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)+1):
            res=i^res
        for num in nums:
            res=res^num
        return res