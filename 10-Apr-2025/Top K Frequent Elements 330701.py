# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has= defaultdict(int)
        res = []
        for i in nums:
            has[i] += 1
        has = dict(sorted(has.items(),key=lambda item:item[1]))

        val = [v for v in has.keys()]
        
        l=len(val)-1
        while k > 0:
            res.append(val[l])
            l-=1
            k-=1
        return res
