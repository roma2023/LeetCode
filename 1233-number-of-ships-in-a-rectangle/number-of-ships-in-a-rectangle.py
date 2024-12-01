# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
        # for the above example, the rectangle has points: 
        # [0,0], [0,4], [4,4], [4,0] 

        # all we need to check if a given point is in the rectangle
        # we know that as long as the point x coord is between [0,4] and 
        # y coord between [0, 4] we can add it into output counter

        # maybe try BS or Divide and Conquer
        def DC(topRight, bottomLeft): 
            if (topRight.x < bottomLeft.x or topRight.y < bottomLeft.y 
                    or not sea.hasShips(topRight, bottomLeft)):
                return 0
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))

            res = 0

            midX = (topRight.x + bottomLeft.x) // 2 
            midY = (topRight.y + bottomLeft.y) // 2 

            TR = Point(0, 0)
            BL = Point(0, 0)

            # for the first quarter
            BL.x, BL.y = midX + 1, midY + 1
            TR.x, TR.y = topRight.x, topRight.y
            res += DC(TR, BL)

            # for the second quarter
            BL.x, BL.y = bottomLeft.x, midY + 1
            TR.x, TR.y = midX, topRight.y
            res += DC(TR, BL)

            # Q3
            BL.x, BL.y = bottomLeft.x, bottomLeft.y
            TR.x, TR.y = midX, midY
            res += DC(TR, BL)

            # Q4
            BL.x, BL.y = midX + 1, bottomLeft.y
            TR.x, TR.y = topRight.x, midY
            res += DC(TR, BL)

            return res

        return DC(topRight, bottomLeft)
