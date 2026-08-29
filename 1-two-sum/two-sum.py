class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                return (i,d[diff])
            d[nums[i]]=i
        