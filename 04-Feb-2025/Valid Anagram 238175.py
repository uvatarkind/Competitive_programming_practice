# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        c={}
        if len(s)!=len(t):
            return False
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in t:
            if x in c:
                c[x]+=1
            else:
                c[x]=1
        for x in d:
            if x not in c:
                return False
            elif d[x]!=c[x]:
                return False
        return True




        