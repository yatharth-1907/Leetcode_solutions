class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        for prefix in range(len(nums)):
            if prefix-1<0:
                answer.append(1) 
            else:
                answer.append(answer[prefix-1]*nums[prefix-1])
        
        suffix=1
        for j in range(len(nums)-1,-1, -1):
            if j+1>=len(nums):
                answer[j]=answer[j]*suffix
            else:
                suffix*=nums[j+1]
                answer[j]=answer[j]*suffix
        return answer
                

        