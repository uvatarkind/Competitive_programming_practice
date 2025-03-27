# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low=0
        high=len(queries)
        def check(mid):
            arr=[0]*(len(nums)+1)
            for i in range(mid):
                left,right,val=queries[i]
                arr[left]+=val
                arr[right+1]-=val
            for i in range(1,len(arr)):
                arr[i]=arr[i-1]+arr[i]

            for i in range(len(nums)):
                if nums[i]-arr[i]>0:
                    return False
            return True

        ans=-1
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans


        
        