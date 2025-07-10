class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniq= set(nums)
        count=0
        element=None
        for i in uniq:
            if nums.count(i)>count:
                count=nums.count(i)
                element=i
        return element
