class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index=[]
        for i in range(len(numbers)-1):
            if i>0 and numbers[i]==numbers[i-1]:
                continue
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]
            
            