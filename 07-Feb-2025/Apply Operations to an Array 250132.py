# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        print(nums)
        for num in nums:
            if num>0:
                ans.append(num)
                print(num)
        while len(ans)!=len(nums):
            ans.append(0)
        return ans
            
