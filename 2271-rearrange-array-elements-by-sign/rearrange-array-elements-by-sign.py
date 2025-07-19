class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
       
        for num in nums:
            if num>=0: 
                positive.append(num)
            else:
                negative.append(num)
        nums.clear()
        for i in range(len(positive)):
            nums.append(positive[i])
            nums.append(negative[i])
                
        return nums