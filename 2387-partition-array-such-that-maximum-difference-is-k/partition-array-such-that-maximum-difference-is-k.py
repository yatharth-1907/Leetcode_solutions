class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            # Extend the group as long as the max - min <= k
            while i < n and nums[i] - start <= k:
                i += 1
            count += 1  # We've formed one group
        return count

            
            