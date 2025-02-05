# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        has={}
        for num in nums:
            if num in has:
                has[num]+=1
            else:
                has[num]=1
        for num in has:
            if has[num]==2:
                ans.append(num)
        return ans
        

        