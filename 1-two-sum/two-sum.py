class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ideation
        # we can cretae a set that stores the differwnces of all target - xi where xi is in nums
        # ex: target = 9, diffs = {7, } and idxMap = {7: [0]} when the next num is 7, we know that we found the match
        # we need to return the idx of two numbers

        diffs = set()
        idxMap = dict()
        for i in range(len(nums)): 
            
            if nums[i] in diffs: 
                return [idxMap[nums[i]], i]
            
            diff = target - nums[i]
            diffs.add(diff)

            # given there is always one exact solution, we dont need a list store all possible inidces
            idxMap[diff] = i


            