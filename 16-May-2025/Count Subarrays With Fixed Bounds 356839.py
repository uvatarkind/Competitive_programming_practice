# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i =  0 # left index
        j = 0  # right index
        ans = 0
        
        minn = [] # store the indices of minK in a window which have no element less than minK and greater than maxK 
        maxx = [] # store the indices of maxK in a window which have no element less than minK and greater than maxK
        
        while j<len(nums):
            if nums[j]==minK:
                minn.append(j)
            if nums[j]==maxK:
                maxx.append(j)

            if nums[j]<minK or nums[j]>maxK: # conflict
                a,b = 0,0 # indices of minn and maxx array
                while a<len(minn) and b<len(maxx):
                    m = max(minn[a],maxx[b])  # max index which should keep in subbarray necessarily
                    ans+=j-m                  # add how many subarray can create such that they start from nums[i]
                    if nums[i]==minK:
                        a+=1
                    if nums[i]==maxK:
                        b+=1
                    i+=1 
                # there is a conflict on indix j so clear minn and maxx array    
                minn.clear()
                maxx.clear()
                
                i = j+1 # set left pointer to j+1 (searching for new window which can start from j+1)
                
            j+=1        
                
        # after reaching j on last indix check if there is a window which is already created       
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
	