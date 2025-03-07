# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count1=0
        for i in range(len(s)):
            if s[i]=='1':
                count1+=1
        count0=len(s)-count1
        new_s=''
        for i in range(len(s)-1):
            if count1>1:
                new_s= new_s+'1'
                count1-=1
            else:
                new_s=new_s+'0'
        new_s=new_s+'1'
        return new_s