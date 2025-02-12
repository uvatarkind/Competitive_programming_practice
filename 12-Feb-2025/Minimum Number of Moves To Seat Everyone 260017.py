# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count=0
        for i in range(len(seats)):
            if seats[i]<=students[i]:
                print(seats[i])
                print(students[i])
                count += (students[i]-seats[i]) 
            elif seats[i]>students[i]:
                count+= (seats[i]-students[i])
            print(count)
        return count