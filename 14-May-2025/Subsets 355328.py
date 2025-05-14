# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        res=[]
        for i in range(2**n):
            temp=[]
            k= 0
            while i>0:
                if i & 1:
                    temp.append(nums[n-k-1])
                k+=1
                i>>=1
            res.append(temp)
        return res

            