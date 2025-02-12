# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        c=0
        print(costs)
        for i in range(len(costs)):
            if count+costs[i]<=coins:
                count= count+costs[i]
                c+=1
                if i == len(costs)-1:
                    return c
            else:
                if count==0:
                    return 0
                else:
                    return c