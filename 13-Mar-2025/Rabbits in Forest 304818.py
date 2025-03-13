# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabits=Counter(answers)
        total=0
        for key,val in rabits.items():

            size=key+1

            group= math.ceil(val/size)
            print(group)

            total+=size*group

        return total