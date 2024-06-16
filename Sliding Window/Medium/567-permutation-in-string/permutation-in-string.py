class Solution:
    # Complexity Analyis
    # TC = O(n)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # find the number of matches in s1 and first s1 chars of s2
        # make a list of all 26 letters
        # if there is a letter, change its val to 1
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # now count the matches
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # this is the sliding window start
        l = 0
        # now we slide
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # find the new index 
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1 
            # if now it matches incrmeent matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # if it mioved away already matching pos then decrement 
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # now do the opposite with the sldiing beginning 
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            # if now it matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # if it used to match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            # and we slide
            l += 1
        return matches == 26
