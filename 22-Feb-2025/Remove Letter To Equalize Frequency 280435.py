# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        frequency = Counter(word)
        counts = list(frequency.values())
        letters = list(frequency.keys())
        unique_counts = list(set(counts))
        if len(unique_counts) > 2:
            return False
        elif len(unique_counts) == 2:
            diff = abs(unique_counts[0] - unique_counts[1])
            minimum = min(unique_counts)
            maximum = max(unique_counts)
            if diff > 1 and (minimum != 1 or (minimum == 1 and counts.count(minimum) > 1)):
                return False
            if diff == 1:
                if (minimum == 1 and counts.count(minimum) > 1 and counts.count(maximum) > 1):
                    return False
                if minimum != 1 and counts.count(maximum) > 1:
                    return False
        elif len(unique_counts) == 1:
            if max(unique_counts) > 1 and len(letters) > 1:
                return False
        return True