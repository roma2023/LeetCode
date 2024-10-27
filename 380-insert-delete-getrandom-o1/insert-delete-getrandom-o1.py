import random
class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.arr = []
        self.last  = 0
        self.size = 0 

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.hashMap[val] = self.size
        self.arr.append(val)
        self.last = val
        self.size += 1	
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        idx = self.hashMap[val]
        self.arr[idx] = self.last
        self.hashMap[self.last] = idx
        self.arr.pop()
        self.size -= 1 
        if self.size > 0:
            self.last = self.arr[self.size - 1]

        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        r = random.randint(0, self.size - 1)
        return self.arr[r]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()