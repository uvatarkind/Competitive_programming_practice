# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent= [i for i in range(len(edges)+1)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            xroot = find(x)
            yroot= find(y)

            if xroot==yroot:
                return False
            parent[yroot]=xroot
            return True
        
        for edge in edges:
            if not union(edge[0],edge[1]):
                return edge
        return []