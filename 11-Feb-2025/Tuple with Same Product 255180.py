# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n= len(nums)
        count=0
        Product_Count= defaultdict(int)
        for i in range(n):
            for j in range(i+1,n):
                product = nums[i]*nums[j]
                Product_Count[product]+=1
        for val in Product_Count.values():
            if val>1:
                count+=((val*(val-1))//2)*8 
        return count