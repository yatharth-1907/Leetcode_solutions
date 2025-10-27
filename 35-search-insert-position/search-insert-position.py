class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=len(nums)
        h=0
        t=len(nums)-1
        mid=(h+t)//2
        while h<=t:
            if nums[mid]>=target:
                ans=min(ans,mid)
            if nums[mid]>target:
                t=mid-1
                
            else:
                h=mid+1
                
            mid=(h+t)//2
        return ans
