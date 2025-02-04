# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans=set()
        for start, end in ranges:
            for i in range(start,end+1):
                ans.add(i)
        for x in range(left,right+1):
            if x not in ans:
                return False
        else:
            return True
                
                    