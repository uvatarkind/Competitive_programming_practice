# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}

        def dp(y):
            if y in memo:
                return memo[y]
            if y==0:
                return 0
            elif y==1 or y==2:
                return 1
            memo[y]= dp(y-1) + dp(y-2) + dp(y-3)  
            return memo[y]
            
        return dp(n) 