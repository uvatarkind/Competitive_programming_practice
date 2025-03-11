# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def cat(n):
            if n==1:
                return "0"
            s= cat(n-1) 
            s2=''
            for i in range(len(s)):
                if s[i]=="0":
                    s2+='1'
                else:
                    s2+='0'
            s2 = s2[::-1]
            return s+'1'+s2
        new=cat(n)
        return new[k-1]
        

