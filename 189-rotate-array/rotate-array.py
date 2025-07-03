class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l==1:
            return nums
        k=k%l
        i=l-k
        new= nums[i:]
        for j in range(l-1,i-1,-1):
            nums.pop(j)
        for k in range(len(new)):
            nums.insert(k,new[k])
        
        
       