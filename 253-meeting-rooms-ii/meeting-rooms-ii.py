import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        
        maxRooms = 1
        prevEnd = intervals[0][1]        
        endQ = [prevEnd]
        heapq.heapify(endQ)
    
        for start, end in intervals[1:]: 
            if start >= prevEnd: 
                prevEnd = end
                endQ = [prevEnd]
                heapq.heapify(endQ)
            else:
                while endQ[0] <= start: # empty rooms till we reach the meeting that has not ended yet
                    heapq.heappop(endQ)

                heapq.heappush(endQ, end)                
                prevEnd = max(prevEnd, end)
                maxRooms = max(maxRooms, len(endQ))
                
        return maxRooms
# TC => O(nlogn). SC => O(n)


        
        
        
        