class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def helper(numss,index):
            sums=0
            string=str(numss)
            for k in string:
                sums+=int(k)
            return sums==index
        for i in range(len(nums)):
            if helper(nums[i],i):
                return i
        return -1
            