# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_sub=0
        left=0
        zero=2
        for right in range(len(nums)):
            if nums[right]==0:
                zero-=1
            
            while zero==0:
                if nums[left]==0:
                    zero+=1
                left+=1
            max_sub=max(max_sub,right-left)
        return max_sub