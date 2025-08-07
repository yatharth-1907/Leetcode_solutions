class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash=defaultdict(int)

        for i in nums:
            hash[i]+=1
        
        avg=len(nums)/3

        ans=[]
        for value, key in hash.items():
            if key>avg:
                ans.append(value)
        return ans