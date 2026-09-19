class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest x coordinate on the rectangle to the circle center
        closestX = max(x1, min(xCenter, x2))
        
        # Find the closest y coordinate on the rectangle to the circle center
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the distance squared from the circle center to this closest point
        distanceX = xCenter - closestX
        distanceY = yCenter - closestY
        distanceSquared = (distanceX ** 2) + (distanceY ** 2)
        
        # Compare squared distance with squared radius to avoid square root
        return distanceSquared <= (radius ** 2)
