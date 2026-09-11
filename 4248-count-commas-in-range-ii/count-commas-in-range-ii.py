class Solution:
    def countCommas(self, n: int) -> int:
        total_comma=0
        threshold=1000
        while n>=threshold:
            total_comma+=(n-threshold+1)
            threshold*=1000
        return total_comma    #second comma

