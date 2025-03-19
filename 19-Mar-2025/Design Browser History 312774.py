# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Dlist:
    def __init__(self,val,next,prev):
        self.val=val
        self.next= next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Dlist(homepage,None,None)
        self.cur = self.head

    def visit(self, url: str) -> None:
        self.cur.next = Dlist(url,None,self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)