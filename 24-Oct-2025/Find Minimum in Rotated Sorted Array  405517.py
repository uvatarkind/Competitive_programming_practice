# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == len(nums)-1:
                return nums[0] 
            elif nums[i] > nums[i+1]:
                return nums[i+1]   