class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        curr_min = float('inf')
        
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            right[i] = curr_min
            
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            if curr_max - right[i] <= k:
                return i
                
        return -1
