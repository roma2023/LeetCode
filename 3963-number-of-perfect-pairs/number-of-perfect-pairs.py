class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # the brute force approach would be to get all possible pairs of indices from the 
        # given array and calculate the conditions we were provided

        #. we need to think of the difference, as we dont really care about the indices to rturn
        # we can just sort them out at the beginning
        # [-3,2,-1,4] => [-3, -1, 2, 4]
        # min(|a - b|, |a + b|) <= min(|a|, |b|) 
        # min(|diff|, |sum|) <= min(|a|, |b|)
        # max(|a - b|, |a + b|) >= max(|a|, |b|)
        # max(|diff|, |sum|) >= max(|a|, |b|)
        # this translates to the pair having the larger and smaller difference and sum 
        # compared to the individual numbers
        # sometimes it is the difference that is larger sometimes the sum is larger
        # but in this case I argue that the pairs (-3, 4) and (3, 4) is the same thing 
        # or equivalent
        # [-3,2,-1,4] <=> [1,2,3,4] 
        # (1,2), (2,3), (2,4), (3,4)
        # [1,10,100,1000] why in this case none of the counts
        # I see the pattern, is it the distance from 0 to the min of the number and diff
        # we can basically only take the absolute values of all given numbers,
        # what about the sum, no worries at all, because their sum is always gonna be higher
        # only check we have to do is on the diff between two
        # so we sort, then check the difference of next element, and only stop till that 
        # difference gets higher than the first/left pointer value, then we add 
        # the length of right-left pointers and shift left pointer to the right by 1, and 
        # repeat our algorithm

        nums = [abs(n) for n in nums]
        nums.sort()

        ans = 0
        left = 0
        for right in range(1, len(nums)):
            while left < right and nums[right] - nums[left] > nums[left]:
                left += 1
            
            ans += max((right - left), 0)
        
        return ans
        