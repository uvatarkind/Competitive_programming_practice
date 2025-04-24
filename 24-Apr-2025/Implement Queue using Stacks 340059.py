# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.que= deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.popleft()

    def peek(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return len(self.que)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()