class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # Count for each of the decrements
        cnt = [0 for _ in range(n + 1)]
        
        # s keeps track of the cumulative sum
        # k num of queries
        s = k = 0

        for i in range(n):
            
            # while the count of the decrements do not add any effect on the nums
            # keep looping 
            while s + cnt[i] < nums[i]:
                k += 1
                # if we overflow
                if k - 1 >= len(queries): return -1
                # take the next query
                l, r, val = queries[k - 1]
                
                # if it ends before us, just continue
                if r < i: continue
                
                # else, take the value and increment the decr effect to mark the start of it
                cnt[max(l, i)] += val
                # marl the end of the decr
                cnt[r + 1] -= val
            s += cnt[i]

            # Time complexity: O(N+M) with N is length of nums and M is length of `queries
            # Space complexity: O(N)
        return k