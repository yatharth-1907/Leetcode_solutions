class Solution:
    def search(self, nums: List[int], target: int) -> int:
       h=0
       t=len(nums)-1
       while h<=t:
           mid=(h+t)//2
           if nums[mid]==target:
               return mid

           if nums[h]<=nums[mid]:
               if nums[h]<=target and target<=nums[mid]:
                   t=mid-1
               else:
                   h=mid+1
           else:
               if nums[mid]<=target and target<=nums[t]:
                   h=mid+1
               else:
                   t=mid-1
       return -1