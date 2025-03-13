# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = []
        result = [0] * len(temp)

        for i in range(len(temp)):
            while stk and temp[i] > temp[stk[-1]]:
                idx = stk.pop()
                result[idx] = i - idx
            stk.append(i)

        return result
