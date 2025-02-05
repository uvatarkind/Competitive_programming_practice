# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], q: List[List[int]]) -> List[int]:
        final=[]
        total=0
        for num in nums:
            if num%2==0:
               total+=num
        for val,index in q:
            if nums[index]%2==0:
                total-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                total+=nums[index]
            final.append(total)
        return final



            
            
    