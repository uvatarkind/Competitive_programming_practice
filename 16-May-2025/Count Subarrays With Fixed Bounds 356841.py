# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i =  0 
        j = 0  
        ans = 0
        
        minn = [] 
        maxx = [] 
        
        while j<len(nums):
            if nums[j]==minK:
                minn.append(j)
            if nums[j]==maxK:
                maxx.append(j)

            if nums[j]<minK or nums[j]>maxK: t
                a,b = 0,0 
                while a<len(minn) and b<len(maxx):
                    m = max(minn[a],maxx[b])  
                    ans+=j-m                  
                    if nums[i]==minK:
                        a+=1
                    if nums[i]==maxK:
                        b+=1
                    i+=1 
                  
                minn.clear()
                maxx.clear()
                
                i = j+1 
                
            j+=1        
                
        
        a,b = 0,0
        while a<len(minn) and b<len(maxx):
            m = max(minn[a],maxx[b])
            ans+=j-m

            if nums[i]==minK:
                a+=1
            if nums[i]==maxK:
                b+=1
             
            i+=1        
                        
        return ans
	