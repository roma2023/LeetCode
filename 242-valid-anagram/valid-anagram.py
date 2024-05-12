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
            

# Complexity Analysis
# Time Complexity = O(n) because we are going through the first list once to create our dictionary, then going over list t once to decrement the frequencies, then again we go over the number of distinct characters  which is gonna be n in the worst case, hence 3n now gives us complexity O(n)
# Space Complexity = O(n) because we are creating a hash table for n elements and their frequencies so at most 2n 