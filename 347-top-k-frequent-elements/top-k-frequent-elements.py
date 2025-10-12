class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so we have to create a freq map
        freqMap = {} # num: freq

        for n in nums: 
            freqMap[n] = freqMap.get(n, 0) + 1
        
        # create a list of num, freq pairs
        freqPairs = []
        for num, freq in freqMap.items(): 
            freqPairs.append([num, freq])

        print(freqPairs)

        # sort the freq Pairs in desc order
        freqPairs = sorted(freqPairs, reverse=True, key=lambda pair: pair[1])

        print(freqPairs)

        
        # return top k
        topK = [freqPairs[i][0] for i in range(k)]

        return topK
