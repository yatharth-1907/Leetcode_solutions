class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_= float(-inf)
        
        for i in range(len(nums)):
            if sum<0:
                sum=0
                
            if sum>=0:
                sum=sum+nums[i]
                max_= max(sum, max_)

        return max_


        