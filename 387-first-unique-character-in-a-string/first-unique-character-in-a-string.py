import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # bucketsort
        buckets = [[] for i in range(len(s) + 1)]

        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else: 
                hashMap[char] += 1
        
        for char in hashMap:
            freq = hashMap[char]
            if freq == 1:
                buckets[freq] += [char]

        if buckets[1] == []:
            return -1

        res = buckets[1][0]
        return s.index(res)
        

        
        
        
                