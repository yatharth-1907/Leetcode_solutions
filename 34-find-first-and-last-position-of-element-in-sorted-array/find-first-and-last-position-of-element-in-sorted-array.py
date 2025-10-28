class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums,target):
            h=0
            t=len(nums)
            ans=len(nums)
            while h<t:
                mid=(h+t)//2
                if nums[mid]>=target:
                    ans=mid
                    t=mid
                else:
                    h=mid+1
            return ans

        def upper_bound(nums,target):
            h=0
            t=len(nums)
            ans=len(nums)
            while h<t:
                mid=(h+t)//2
                if nums[mid]>target:
                    ans=mid
                    t=mid
                else:
                    h=mid+1
            return ans-1

        first=lower_bound(nums,target)
        if first==len(nums) or nums[first]!= target:
            return [-1,-1]
        return [first,upper_bound(nums,target)]

      