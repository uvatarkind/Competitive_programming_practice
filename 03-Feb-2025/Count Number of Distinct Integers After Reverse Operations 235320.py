# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev=[]
        ans=set()
        for i in nums:
            rev.append(int(str(i)[::-1]))
        for i in range(len(nums)):
            ans.add(rev[i])
            ans.add(nums[i])
        return len(ans)
        
        