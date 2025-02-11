# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        summ=0
        l=0
        r=len(piles)-1
        piles=sorted(piles)
        print(piles)
        while l<r-1:
            summ+=piles[r-1]
            r-=2
            l+=1
        return summ
        

        