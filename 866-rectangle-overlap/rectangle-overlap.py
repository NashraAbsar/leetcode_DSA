class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not      (         #saari non-overlap ki condn hain
        rec1[2]<=rec2[0] or    #rec1 ka r phele h rec2 ke l se
        rec1[0]>=rec2[2] or      #rec1 ka l badme h rec2 ke r se
        rec1[3]<=rec2[1] or      #rec1 ka top neeche h rec2 ke bottom se
        rec1[1]>=rec2[3])      #rec1 ka bottom upr h rec2 ke top se

        