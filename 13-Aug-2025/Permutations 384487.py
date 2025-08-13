# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # make a copy
                return
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used.remove(i)

        backtrack([], set())
        return res
