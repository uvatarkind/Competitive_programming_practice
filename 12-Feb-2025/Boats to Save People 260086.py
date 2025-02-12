# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people) - 1
        boats = 0
        while start <= end:
            weight = people[start] + people[end]
            if weight <= limit:
                start += 1
            boats += 1
            end -= 1
        return boats