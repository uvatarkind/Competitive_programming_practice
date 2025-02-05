# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(" ")
        mx=0
        x=0
        res=[]
        for i in s:
            mx= max(mx,len(i))
        for x in range(mx):
            new=""
            for i in s:
                if x < len(i):
                    new+=i[x]
                else:
                    new+=" "
            res.append(new.rstrip())
        return res
        







        
        