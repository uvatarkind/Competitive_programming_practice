# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        count=0
        summ=0
        l=0
        r=len(skill)-1
        while l<=r:
            count=skill[l]+skill[r]
            summ+=(skill[l]*skill[r])
            l+=1
            r-=1
            if count!=skill[l]+skill[r]:
                return -1
        return summ