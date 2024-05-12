class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        wordFreq = dict()
        for i in range(len(s)): 
            wordFreq[s[i]] = wordFreq.get(s[i], 0) + 1 
            wordFreq[t[i]] = wordFreq.get(t[i], 0) - 1

        # check if all the freqs are 0
        for word in wordFreq:
            if wordFreq[word] != 0:
                return False
        return True 
