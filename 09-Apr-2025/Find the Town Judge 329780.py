# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1

        has1={}
        has2={}
        for i in range(len(trust)):
            if trust[i][0] not in has1:
                has1[trust[i][0]]=1
            else:
                has1[trust[i][0]]+=1
        
        for i in range(len(trust)):
            if trust[i][1] not in has2:
                has2[trust[i][1]]=1
            else:
                has2[trust[i][1]]+=1
        for key, val in has2.items():
            if key not in has1 and val==n-1:
                return key
        return -1
       

       
