# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        has={}
        ans=[]
        for i in nums :
            if i in has:
                has[i]+=1
            else:
                has[i]=1
        for i in has:
            if has[i]==2:
                ans.append(i)
        return ans
                

        