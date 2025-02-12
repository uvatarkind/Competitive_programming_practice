# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res= 0
        l= 0
        r= len(height)-1
        while r!=l:
            a= (r-l)* min(height[r], height[l])
            res= max(a,res)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return res