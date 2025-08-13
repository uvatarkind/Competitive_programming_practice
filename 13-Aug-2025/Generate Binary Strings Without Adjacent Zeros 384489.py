# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n):
        res = []

        def backtrack(path):
            if len(path) == n:
                res.append("".join(path))
                return

            path.append('1')
            backtrack(path)
            path.pop()

            if not path or path[-1] != '0':
                path.append('0')
                backtrack(path)
                path.pop()

        backtrack([])
        return res
