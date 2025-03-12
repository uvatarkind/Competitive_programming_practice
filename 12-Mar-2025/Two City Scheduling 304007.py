# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[1] - cost[0])
        total=0
        for i in range(len(costs)):
            if i<(len(costs)/2):
                total+=costs[i][1]
            else:
                total+=costs[i][0]
        return total
