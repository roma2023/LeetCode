class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [None] * (n+2)

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        if id == self.ptr:
            while self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[id:self.ptr]
        return []