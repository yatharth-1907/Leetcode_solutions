class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        delta= [0]*(n+1)

        for l,r in queries:
            delta[l]-=1
            if r+1 <n:
                delta[r+1]+=1
        curr=0
        for i in range(n):
            # if nums[i]==0:
            #     continue
            curr+=delta[i]
            nums[i]+=curr
            if nums[i]>0:
                return False
        return True 

        