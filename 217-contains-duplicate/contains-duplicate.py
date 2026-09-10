class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums)!=len(set(nums)))  # ya phir loop lage ek ek elem