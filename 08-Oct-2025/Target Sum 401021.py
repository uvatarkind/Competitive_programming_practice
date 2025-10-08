# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo=defaultdict(int)
        def dp(index, val):
            add = minus = 0
            if index==len(nums) and val== target:
                return 1
            
            if (index,val) in memo:
                return memo[(index,val)]

            if index<len(nums):
                add= dp(index+1,val+nums[index])
                minus= dp(index+1,val- nums[index])

            memo[(index,val)] = add+minus

            return add+minus
              
            

        return dp(0,0)

            
           
