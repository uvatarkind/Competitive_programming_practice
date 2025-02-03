# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=collections.Counter(words[0])
        for word in words:
            ans &=collections.Counter(word)
        return list(ans.elements())    