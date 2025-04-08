# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[]
        i=0
        while i <n:
            c = nums[i] -1
            if nums[i] != nums[c]:
                nums[i], nums[c]= nums[c],nums[i]
            else:
                i+=1
        for i in range(n):
            if i+1!= nums[i]:
                arr.append(i+1)

        return arr

                
