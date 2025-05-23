# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        dq = deque()
        n = len(deck)
        dq.appendleft(deck[0])
        for i in range(1, n):
            x = dq.pop()
            dq.appendleft(x)
            dq.appendleft(deck[i])

        ans = []
        while dq:
            ans.append(dq.popleft())
        return ans