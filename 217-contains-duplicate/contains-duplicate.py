class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set(nums)
        if len(Set) != len(nums):
            return True
        return False