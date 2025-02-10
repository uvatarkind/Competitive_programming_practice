# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        k=list(map(str,nums))
        k.sort(key=lambda x:x*10,reverse=True)
        if k[0]=='0':
            return '0'
        return ''.join(k)
        


        