# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk=[]
        stk2=[]
        for i in range(len(s)):
            if s[i]=='#':
                if stk:
                    stk.pop()
            else:
                stk.append(s[i])
        for i in range(len(t)):
            if t[i]=='#':
                if stk2:
                    stk2.pop()
            else:
                stk2.append(t[i])
        if stk==stk2:
            return True
        else:
            return False

        