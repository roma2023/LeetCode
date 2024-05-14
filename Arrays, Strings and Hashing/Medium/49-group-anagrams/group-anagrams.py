class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
        anagrams = defaultdict(list)

        for word in strs: 
            signature = [0] * 26
            for char in word: 
                signature[ord(char) - ord('a')] += 1
            anagrams[tuple(signature)] += [word]
        return anagrams.values()
