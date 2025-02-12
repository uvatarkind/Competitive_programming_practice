# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=0
        r=len(num)-1
        while l<r:
            if num[l]+num[r]==target:
                return [l+1,r+1]
            elif num[l]+num[r]<target:
                l+=1
            elif num[l]+num[r]>target:
                r-=1
        