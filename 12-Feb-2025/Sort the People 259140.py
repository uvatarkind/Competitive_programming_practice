# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_heights = sorted(zip(names,heights),key=lambda x:x[1],reverse=True)
        return [name for name,height in name_heights]