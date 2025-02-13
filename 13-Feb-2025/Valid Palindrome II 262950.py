# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        new=s[::-1]
        left=0
        right=len(s)-1
        if s== new:
            return True
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                sl = s[left + 1: right + 1]
                sr= s[left:right]
                if sl==sl[::-1] or sr==sr[::-1]:
                    return True
                return False
        return True
                
        