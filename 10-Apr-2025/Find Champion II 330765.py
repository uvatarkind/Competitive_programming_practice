# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n  

        for u, v in edges:
            in_degree[v] += 1 

        champions = [i for i in range(n) if in_degree[i] == 0]

        return champions[0] if len(champions) == 1 else -1
