class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        max=nums[0]             
        for i in range(0,n):
            if nums[i]>max:
                max=nums[i]
            min=float('inf')
            for j in range(i,n):
                if nums[j]<min:
                    min=nums[j]
            if (max-min)<=k:
                return i
        return -1