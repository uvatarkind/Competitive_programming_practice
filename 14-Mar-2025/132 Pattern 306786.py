# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        mx = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mx:
                return True
            while stk and stk[-1] < nums[i]:
                mx = stk[-1]
                stk.pop()
            stk.append(nums[i])
        return False