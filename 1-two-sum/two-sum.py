class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2= target-nums[i]
            new_n= nums[i+1:]
            if num2 in new_n:
                index= i+new_n.index(num2)+1
                return [i,index]
                
