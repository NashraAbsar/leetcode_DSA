class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each value with its original index
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        groups = []
        current_group = []
        
        for val, idx in indexed_nums:
            if not current_group or val - current_group[-1][0] <= limit:
                current_group.append((val, idx))
            else:
                groups.append(current_group)
                current_group = [(val, idx)]
        
        if current_group:
            groups.append(current_group)
            
        res = [0] * n
        for group in groups:
            # Extract indices and values from the group
            indices = sorted(idx for _, idx in group)
            values = sorted(val for val, _ in group)
            
            # Assign sorted values to sorted original indices
            for i, val in zip(indices, values):
                res[i] = val
                
        res = res # just to be clear
        return res
