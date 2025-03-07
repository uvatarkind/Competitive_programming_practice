# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if i>mx:
                return False
            mx=max(mx,i+nums[i])

            if mx >=len(nums)-1:
                return True
        return False

