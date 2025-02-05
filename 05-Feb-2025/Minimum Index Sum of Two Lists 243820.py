# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1={}
        ans=[]
        mn= float('inf')
        for i in range(len(list1)):
            l1[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in l1:
                curr= j + l1[list2[j]]
                if curr < mn:
                    mn=curr
                    ans=[]
                    ans.append(list2[j])
                elif curr==mn:
                    ans.append(list2[j])
        return ans
        