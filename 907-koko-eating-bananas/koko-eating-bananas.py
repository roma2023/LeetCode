class Solution:
    # Complexity Analysis
    # TC = (log(max(piles)) * len(piles))
    # SC = O(len(piles))
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # we have left and right vals
        l, r = 1, max(piles)
        res = r

        # while l not greater than the max val
        while l <= r:
            # find mid val
            k = (l + r) // 2

            # count the hours
            totalTime = 0
            # find totalTime for all piles
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            # if total time is less than / equal the given h
            # then save it in res and move r to mid - 1
            if totalTime <= h:
                res = k
                r = k - 1
            # else move l to mid + 1
            else:
                l = k + 1
        # this guarantees the min speed
        return res
