# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        arr=[]
        new=[]
        nums.sort()
        count=Counter(nums)
        for i in range(1,len(nums)+1):
            new.append(i)
        for key, val in count.items():
            if val==2:
                arr.append(key)
        for num in new:
            if num not in nums:
                arr.append(num)
        return arr