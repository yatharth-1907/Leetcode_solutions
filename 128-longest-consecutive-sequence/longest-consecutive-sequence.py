import sys 
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        longest=0
        last= sys.maxsize
        count=0


        for num in nums:

            if num-1== last:
                count+=1
                last= num

            elif num != last:
                last= num
                count=1
            longest= max(longest,count)

        return longest

            