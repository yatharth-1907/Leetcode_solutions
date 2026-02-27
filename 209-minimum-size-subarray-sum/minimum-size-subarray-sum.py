class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        i,j=0,0
        curr_sum=0
        while j<len(nums) and i<len(nums):
            curr_sum+=nums[j]
            if curr_sum==target:
                min_len=min(min_len,j-i+1)
                j+=1
            elif curr_sum>target:
                min_len=min(min_len,j-i+1)
                curr_sum-=nums[i]+nums[j]
                i+=1
            else:
                j+=1
        return min_len if min_len!= float('inf') else 0

