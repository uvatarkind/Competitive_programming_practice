# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        ans=""
        has= Counter(s)
        new=sorted(has.items(), key=lambda x: x[1], reverse=True)
        for k,v in new:
            ans+= k *v
        return ans