# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        has={}
        ans=[]
        for x in cpdomains:
            x=x.split()
            rep=int(x[0])
            domain=x[1].split(".")
            for d in range(len(domain)):
                subdom= ".".join(domain[d:])
                if subdom in has:
                    has[subdom]+=rep
                else:
                    has[subdom]=rep
        for d in has:
            ans.append(str(has[d])+" "+ d)
        return ans 