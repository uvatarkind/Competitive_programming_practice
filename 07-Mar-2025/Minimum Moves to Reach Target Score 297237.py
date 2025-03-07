# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        answer=0 
        while target>1:
            if maxDoubles>0:
                if target%2==0:
                    target=target//2
                    maxDoubles-=1
                else:
                    target-=1
                answer+=1
            else:
                answer +=(target-1)
                break
        return answer