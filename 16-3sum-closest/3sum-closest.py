class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while(j<k):
                addition=nums[i]+nums[j]+nums[k]
                if abs(target-closest)> abs(target-addition):
                    closest= addition 

                if addition >target:
                    k-=1
                
                elif addition < target:
                    j+=1

                else: 
                    return addition 
        return closest
                