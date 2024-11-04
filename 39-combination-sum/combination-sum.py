class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            
        def find(path, i, curr_sum, target):
            if  i >= len(candidates) or curr_sum > target: return []
            if curr_sum == target: return [path]
            return [] + find(path + [candidates[i]], i, curr_sum + candidates[i], target) + find(path, i + 1, curr_sum, target)
        
        return find([], 0, 0, target)