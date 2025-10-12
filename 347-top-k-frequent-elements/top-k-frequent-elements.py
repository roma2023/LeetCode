class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use algo bucketsort, where we will create a freq list of size n + 1
        # where each index will represent a freq, then when we traverse the freqmap 
        # we can store the numbers at idx = freq
        # afterwards we will through the bucket right to left to retrieve k elements

        freqmap = {}

        for n in nums: 
            freqmap[n] = freqmap.get(n, 0) + 1

        bucket = [[] for i in range(len(nums)+1)]
        for num, freq in freqmap.items():
            bucket[freq].append(num)


        result = []

        for i in range(len(nums), 0, -1):
            b = bucket[i]
            if len(b) > k: 
                result = result + b[:k]
                return result
            
            result = result + b
            k -= len(b)
        
        return result
        
# TC => O(n)
# SC => O(n)