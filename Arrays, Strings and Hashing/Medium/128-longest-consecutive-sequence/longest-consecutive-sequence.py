class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        Set = set(nums)
        Max = 0
        for num in nums:
            counter = 0
            if num-1 not in Set: 
                while num+counter in Set:
                    counter += 1
            Max = max(Max, counter)
        return Max

"""
complexity analysis, time complexity O(n) we will go over the list at most twice
space complexity, as we are creating a set of the size n, the complexity is O(n)
"""