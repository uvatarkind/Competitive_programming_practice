# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans0=[]
        ans1=[]
        d={}
        c=set()
        for winner,losser in matches:
            c.add(winner)
            c.add(losser)
            if losser in d:
                d[losser]+=1
            else:
                d[losser]=1
        print(d)
        for x in c:
            if x not in d:
                ans0.append(x)
            else:
                if d[x]==1:
                    ans1.append(x)
        ans=[]
        ans.append(sorted(ans0))
        ans.append(sorted(ans1))
        return ans



        