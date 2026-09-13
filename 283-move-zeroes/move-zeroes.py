class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_nonzero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_nonzero],nums[i]=nums[i],nums[last_nonzero]
                last_nonzero+=1