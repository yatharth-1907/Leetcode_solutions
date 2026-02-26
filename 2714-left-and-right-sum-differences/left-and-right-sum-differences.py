class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rsum=[]
        lsum=[]
        l,r=0,0

        for i in nums:
            l=l+i
            lsum.append(l)

        for j in nums[::-1]:
            r=r+j
            rsum.append(r)
        rsum= rsum[::-1]
        for i in range(len(nums)):
            nums[i]=abs(lsum[i]-rsum[i])
        return nums
        