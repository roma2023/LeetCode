class Solution:
    # Complexity Analysis
    # TC = O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # checking in set is O(1)
            while s[r] in charSet:
                # remove and add O(1)
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
