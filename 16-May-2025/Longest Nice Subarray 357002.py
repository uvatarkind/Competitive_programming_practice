# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        count=Counter()
        left=0
        right=0
        n=len(nums)
        maxsub=0
        for right in range(n):
            num=nums[right]
            for i in range(32):
                if num & (1<<i):
                    count[i]+=1
            while any(v >1 for v in count.values()):
                for i in range(32):
                    if nums[left] & (1<<i):
                        count[i]-=1
                left+=1
            maxsub=max(maxsub,right-left+1)
        return maxsub