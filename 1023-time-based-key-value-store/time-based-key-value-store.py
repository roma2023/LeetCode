class TimeMap:
    # Complexity Analysis
    # TC = O(logn)  SC = O(n) <-2n
    def __init__(self):
        """
        Initialize a diictionary/hashmap
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    # save the key and value as a list of lists
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    # get the values list for matching key
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, []) # [] is a default val
        
        # binary search 
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # if timestamp matches or less then save in res
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)