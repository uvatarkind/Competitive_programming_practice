# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nums = list(range(1, n + 2))  # start with smallest digits
        
        i = 0
        while i < n:
            if pattern[i] == 'D':
                start = i
                while i < n and pattern[i] == 'D':
                    i += 1
                end = i
                nums[start:end+1] = reversed(nums[start:end+1])
            else:
                i += 1
        
        return ''.join(map(str, nums))
