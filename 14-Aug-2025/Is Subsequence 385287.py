# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    
        if s==t or s=='':
            return True
        if len(s)==len(t) and s!=t:
            return False
        left=0
            
        for right in range(len(t)):
            if s[left]==t[right]:
                left+=1
            if left==len(s):
                return True
        return False

            
        
