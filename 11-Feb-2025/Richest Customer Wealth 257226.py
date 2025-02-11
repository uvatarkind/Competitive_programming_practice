# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx=0
        for i in range(len(accounts)):
            summ=0
            for j in range(len(accounts[0])):
                summ+=accounts[i][j]
            mx=max(summ,mx)
        return mx