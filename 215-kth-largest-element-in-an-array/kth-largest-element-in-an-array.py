import functools
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negList = list(map(lambda x: -x, nums))
        heap = heapq.heapify(negList)
        ret = 0 
        while k: 
            k -= 1
            ret = heapq.heappop(negList)
        return -ret