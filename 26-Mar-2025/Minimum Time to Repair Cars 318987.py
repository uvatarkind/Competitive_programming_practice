# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mn=1
        mx= max(ranks)*(cars**2)

        def check(mid):
            car=0
            for rank in ranks:
                car+=int((mid/rank)**0.5)
                if car>=cars:
                    return True
            return False
        print(mn)  
        print(mx)         
        while mn<=mx:
            mid=(mn+mx)//2
            if check(mid):
                mx=mid-1
            else:
                mn=mid+1
        return mn

             

