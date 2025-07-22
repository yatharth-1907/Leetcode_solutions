class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        sum= 0
        count=0
        hashmap[0]=1

        for num in nums:
            sum+=num
            if sum-k in hashmap:
                count+=hashmap[sum-k]
            hashmap[sum]+=1
        
        return count
