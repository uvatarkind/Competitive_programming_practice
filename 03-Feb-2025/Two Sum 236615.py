# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        count=0
        for i, num in enumerate(nums):
            if target - num in ht:
                return [ht[target - num], i]
                count+=1
            ht[num] = i
            
        return count