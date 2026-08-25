class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert to set for O(1) lookups
        num_set = set(nums)
        
        # Start with the first positive multiple of k
        multiple = k
        
        # Increment by k until the multiple is missing from the set
        while multiple in num_set:
            multiple += k
            
        return multiple
