class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]  # Shift the larger element one position to the right
                j -= 1
            nums[j + 1] = key  # Insert the key in the right place
