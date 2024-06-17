class Solution:
    # TC = O(n)
    def minWindow(self, s: str, t: str) -> str:
        # if the t is empty, return it
        if t == "":
            return ""
        
        # Make countT. a stable hs to compare the window with 
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have - count of target chars
        # need - needed count
        have, need = 0, len(countT)

        # res - range of string
        # resLen - length of string, inf by default
        res, resLen = [-1, -1], float("infinity")

        # left and right pointers
        l = 0
        for r in range(len(s)):
            c = s[r]
            # add char into window
            window[c] = 1 + window.get(c, 0)

            # if its in the count and we have correct number 
            # increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            # if we reached the have==need, save res and 
            # pop from left till its invalid
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        # if found return string, if still inf return empty string
        return s[l : r + 1] if resLen != float("infinity") else ""
