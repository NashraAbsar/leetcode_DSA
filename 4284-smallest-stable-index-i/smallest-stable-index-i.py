class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        right=[0]*n
        minn=float('inf')
        maxx=float('-inf')
        for i in range(n-1,-1,-1):
            right[i]=min(minn,nums[i])
            minn=min(minn,nums[i])
        for r in range(len(right)):
            maxx=max(maxx,nums[r])
            if maxx-right[r]<=k:
                return r
        return -1
        