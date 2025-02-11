# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        has=Counter(s)
        freq=Counter(has.values())
        for k, v in freq.items():
            if k*v!=len(s):
                return False
            else:
                return True