# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[""]*len(s)
        for index,char in enumerate(s):
            ans[indices[index]]= char
        return "".join(ans)