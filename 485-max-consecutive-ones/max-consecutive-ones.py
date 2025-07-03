class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j=0,0
        count=0
        max_=0
        while (j<len(nums)):
            if(nums[i]==nums[j]==1):
                count+=1
                max_=max(max_,count)
            else:
                i=j+1
                count=0
            j+=1
        return max_

