class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        post=0
        neg=1
        for i in nums:
            if i>0:
                ans[post]=i
                post=post+2
            else:
                ans[neg]=i
                neg=neg+2
        return ans

        
        