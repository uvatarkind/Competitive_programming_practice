# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        minArrow=1
        currEnd=points[0][1]
        
        for i in range(1,len(points)):
            if points[i][0]>currEnd:
                
                minArrow+=1
                currEnd=points[i][1]
        return minArrow
