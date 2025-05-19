# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        def rec(arr,k,i):
                if len(arr)==1:
                    return arr[0]
                else:
                    i=(i+k-1)% len(arr)
                    arr.pop(i)
                    return rec(arr,k,i)
                

        ans= rec(arr,k,0)
        print(ans)
        return ans