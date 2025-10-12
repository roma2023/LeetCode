class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
# Complexity 
# TC => O(m * nlogn) m is the numnber of strings, n is the length of the longest string
# SC => O(m * n) for new strings mn and hashmap mn
