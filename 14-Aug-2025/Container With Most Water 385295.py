# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        mx_water=0
        while left<right:
            width= right-left
            length= min(height[left],height[right])
            if width*length>= mx_water:
                mx_water= width*length
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return mx_water