# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:
    def __init__(self, n: int):
        self.unres=[i for i in range(1,n+1)]
        self.res=[]
        heapq.heapify(self.res)
        heapq.heapify(self.unres)


    def reserve(self) -> int:
        reser= heapq.heappop(self.unres)
        heapq.heappush(self.res, reser)
        return reser

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappop(self.res)
        heapq.heappush(self.unres, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)