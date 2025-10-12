class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # cretae  ahasMap of all, then store the indices in the hashMap of hashmaps mapped to list of indices
        A = dict()
        for s in strs: 
            H = self.createHash(s)
            A[H] = A.get(H, [])
            A[H].append(s)

        # combine groups into a list
        results = []
        for h, g in A.items(): 
            results.append(g)
        return results
        
    def createHash(self, s: str) -> dict(): 
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        return tuple(count)

# Complexity 
# TC => O(m * nlogn) m is the numnber of strings, n is the length of the longest string
# SC => O(m * n) for new strings mn and hashmap mn
