# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        countR = countL =count=0
        for i in range(len(s)):
            if s[i]=='R':
                countR+=1
            else:
                countL+=1
            if countR==countL:
                count+=1
        return count
              