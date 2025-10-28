class Tree:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Tree(homepage, None, None)
        self.current = self.history
        

    def visit(self, url: str) -> None:
        next = Tree(url, None, self.current)
        self.current.next = next
        self.current = self.current.next
        #print("current: ", self.current.val)

    def back(self, steps: int) -> str:
        while self.current != self.history and steps != 0:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
        

    def forward(self, steps: int) -> str:
        while self.current.next != None and steps != 0:
            steps -= 1
            self.current = self.current.next
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)