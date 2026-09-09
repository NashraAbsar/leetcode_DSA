class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        start = 1
        
        # Iterate through intervals based on number of digits
        while start <= n:
            # Determine the number of digits for the current range
            length = len(str(start))
            # The upper bound for the current digit length
            end = min(n, 10**length - 1)
            
            # Number of commas in each number of this length
            commas_per_num = (length - 1) // 3
            
            # How many numbers exist in this digit length range
            count = end - start + 1
            
            # Accumulate the total comma count
            total_commas += count * commas_per_num
            
            # Move to the next digit level (e.g., 1 -> 10 -> 100 -> 1000)
            start = 10**length
            
        return total_commas
