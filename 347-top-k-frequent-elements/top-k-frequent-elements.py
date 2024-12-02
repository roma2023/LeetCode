
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         bucket = [[] for i in range(len(nums) + 1)]

#         for num in nums: 
#             count[num] = count.get(num, 0) + 1
#         for num, freq in count.items(): 
#             bucket[freq].append(num)
        
#         res = []
#         print(bucket)
#         for i in range(len(nums), 0, -1): 
            
#             for num in bucket[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res

    # Bucket sort: O(n) time and O(n) space complexity
    # Max Heap: O(n + klogn) time and O(n) space complexity      
    # Sorting: O(nlogn) time and O(n) space complexity
    # Counter in Python: O(n + klogn) time and O(n + k) space complexity 
    
    #        counter = Counter(nums)
    #        return [num for num, _ in counter.most_common(k)]

    # Quick Select Algo O(n)

##

from collections import Counter
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq_tab = list(count.values())   
        
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, right = [], []
            for num in nums:
                if num >= pivot:
                    left.append(num)
                else:
                    right.append(num)
            
            if len(left) == k:
                return left
            elif len(left) > k:
                return quickSelect(left, k)
            else:
                return quickSelect(right, k - len(left)) + left
        
        index = quickSelect(freq_tab, k)
        return [key for key, val in count.items() if val in index]