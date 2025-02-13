# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        has=defaultdict(int)
        for i in range(len(s)):
            if s[i] in has:
                has[s[i]]=i
            l=0
            mx=0
            ans=[]
            for r in range(len(s)):
                mx = max(mx,has[s[r]])
                if mx == r:
                    ans.append(r-l+1)
                    l = r + 1
        return ans