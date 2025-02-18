# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k > 0:
            nums.reverse()
            l = 0
            r = k-1
            while r>=l:
                nums[r],nums[l]= nums[l],nums[r]
                l,r = l+1,r-1
            l,r = k,len(nums)-1
            while r>=l:
                nums[r],nums[l]= nums[l],nums[r]
                l,r = l+1,r-1 