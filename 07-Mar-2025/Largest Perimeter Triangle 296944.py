# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-1
        while n-2>=0:
            a=nums[n] 
            b=nums[n-1]
            c=nums[n-2]
            if b+c>a:
                return a+b+c
            else:
                n-=1
        return 0
            
        