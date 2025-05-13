# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn= deque()
        left =0
        right=0
        res=0
    
        for right in range(len(nums)):
            while mx and nums[right] > mx[-1]:
                mx.pop()
            mx.append(nums[right])

            while mn and nums[right]<mn[-1]:
                mn.pop()
            mn.append(nums[right])

            while mx[0] - mn[0]> limit:

                if nums[left] == mx[0]:
                    mx.popleft()
                if nums[left] == mn[0]:
                    mn.popleft()
                left += 1  

            res = max(res, right - left + 1)

        return res