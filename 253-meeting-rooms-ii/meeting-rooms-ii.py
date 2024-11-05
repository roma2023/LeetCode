import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        endQ = []
        rooms = 1

        print(intervals)


        prevEnd = intervals[0][1]
        endQ.append(prevEnd)
        
        heapq.heapify(endQ)

        maxRooms = 1
        
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
                
                print(maxRooms, start, endQ)

        
        return maxRooms
        


        
        
        
        