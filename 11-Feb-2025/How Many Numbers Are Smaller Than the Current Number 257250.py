# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        List = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(j != i and nums[j] < nums[i]):
                    count = count + 1
            List.append(count)
        return List
