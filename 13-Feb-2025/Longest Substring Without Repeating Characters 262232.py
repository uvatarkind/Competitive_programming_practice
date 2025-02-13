# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx=0
        l=0
        has=set()
        for i in range(len(s)):
            while s[i] in has:
                has.remove(s[l])
                l+=1
            has.add(s[i])
            mx=max(mx,i-l+1)
        return mx
                 