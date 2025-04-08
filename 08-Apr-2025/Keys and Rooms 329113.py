# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            visited.add(node)
            for v in rooms[node]:
                if v not in visited:
                    dfs(v)
        dfs(0)
        return len(visited) == len(rooms)