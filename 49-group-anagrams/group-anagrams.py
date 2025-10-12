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
        # H = dict()
        # for char in s: 
        #     H[char] = H.get(char, 0) + 1

        # map the hash into string
        H = sorted(s)
        H = "".join(H)        
        return H
