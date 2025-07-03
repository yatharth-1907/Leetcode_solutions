class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=len(nums)
        es=sum(nums)
        s=(m*(m+1))//2
        return(s-es)