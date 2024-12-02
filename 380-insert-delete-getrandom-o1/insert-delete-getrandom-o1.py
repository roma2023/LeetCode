import random
class RandomizedSet:

    def __init__(self):
        self.hashMap = {} # key:val => val:idx 
        self.array = [] # array is used for the random function
        self.size = 0 #  size of the array

    def insert(self, val: int) -> bool:
        # returns true if item was not there, else false
        if val in self.hashMap:
            return False
        self.hashMap[val] = self.size
        self.array.append(val)
        self.size += 1
        return True


    def remove(self, val: int) -> bool:
        # returns true if item was there, else false
        if val not in self.hashMap:
            return False
        idx = self.hashMap[val]
        if idx == self.size - 1: 
            self.array.pop()
        else:
            last = self.array[self.size-1]
            self.array[idx] = last
            self.array.pop()
            self.hashMap[last] = idx
        
        del self.hashMap[val]
        self.size -= 1
        # print(self.hashMap, self.array)
        return True

    def getRandom(self) -> int:
        # returns a random int with the same probability
        idx = random.randint(0, self.size - 1)
        return self.array[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()