class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get the signature of the string in a list size of 26
        # then store the signature as a key in hashtable and words list as a value

        anagrams = defaultdict(list)

        for word in strs: 
            signature = [0] * 26
            for char in word: 
                signature[ord(char) - ord('a')] += 1
            anagrams[tuple(signature)] += [word]
        return anagrams.values()

        # time complexity O(26 * n * m).  n for iteration and m is for getting a signature
        # space complexity O(26 * n * m), everytime we get signature we make a copy of string in meemory of size m, and we have n such strings 