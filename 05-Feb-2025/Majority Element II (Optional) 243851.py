# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=float(len(nums))
        freq={}
        ans=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in freq:
            if freq[num]> n/3:
                ans.append(num)
        return ans
        