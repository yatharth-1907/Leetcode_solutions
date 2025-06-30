class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        left=0
        
        for right in range(len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                count=max(count,right-left+1)
        return count
