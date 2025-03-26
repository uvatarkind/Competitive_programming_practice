# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        
        def check(mid):
            day=1
            curr=0
            for weight in weights:

                if curr + weight > mid:
                    curr = weight
                    day += 1
                else:
                    curr += weight
            return day <= days

        while low<=high:
            mid=(low+high)//2
            if check(mid):
                high=mid-1
            else:
                low=mid+1
        return low


           