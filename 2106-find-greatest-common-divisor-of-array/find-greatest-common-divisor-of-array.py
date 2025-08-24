class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smaller= min(nums)
        larger= max(nums)
        ans=0

        while smaller!=0:
            ans=smaller
            smaller= larger%smaller
            larger= ans
        return ans