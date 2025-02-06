# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = defaultdict(list)

        for word in strs:
            key="".join(sorted(word))
            anagram[key].append(word)
        return list(anagram.values())
        