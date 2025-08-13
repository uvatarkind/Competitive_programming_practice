# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def can_place(d):
            count = 1  # first ball in first basket
            last = position[0]
            for pos in position[1:]:
                if pos - last >= d:
                    count += 1
                    last = pos
                    if count >= m:
                        return True
            return False

        low, high = 1, position[-1] - position[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
