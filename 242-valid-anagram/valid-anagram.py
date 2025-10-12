class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if they are of same length
        if len(s) != len(t):
            return False
        
        # create hashsets for both strings
        hashSetS, hashSetT = dict(), dict()
        for i in range(len(s)): 
            hashSetS[s[i]] = hashSetS.get(s[i], 0) + 1
            hashSetT[t[i]] = hashSetT.get(t[i], 0) + 1
        
        # check hashSet for exact match
        if hashSetS != hashSetT:
            return False
        return True


        