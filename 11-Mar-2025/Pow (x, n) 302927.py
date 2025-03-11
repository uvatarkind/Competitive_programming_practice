# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            return pow(x,n)
        elif n<0:
            return pow(x,n)
        else:
            return 1