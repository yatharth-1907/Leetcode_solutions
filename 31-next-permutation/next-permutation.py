class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=-1
        n=len(nums)
        for i in range(n-2, -1,-1):
            if nums[i]< nums[i+1]:
                flag=0
                break
        if flag==-1:
            nums.reverse()
            return nums
        
        for large in range(n-1, -1,-1):
            if nums[large]> nums[i]:
                nums[large],nums[i]=nums[i],nums[large]
                break
        
        nums[i+1:] = nums[i+1:][::-1]
        return nums