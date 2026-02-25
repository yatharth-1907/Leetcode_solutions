class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}
        i=0
        while i<len(nums):
            if nums[i] in hash:
                if abs(hash[nums[i]]-i)<=k:
                    return True
                hash[nums[i]]=i
                i+=1
            else:
                hash[nums[i]]=i
                i+=1
        return False