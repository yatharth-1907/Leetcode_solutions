class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l= len(nums)-1
        nums.sort()
        left,right= 0,l
        power=[1]*(l+1)
        mod=10**9 +7
        count=0

        #precomputer the power
        for i in range(1,l+1):
            power[i]= (power[i-1]*2)% mod

        while left<=right:
            if nums[left]+nums[right]<=target:
                count=(count+power[right-left])%mod
                left+=1
            else:
                right-=1
                
        return count
            