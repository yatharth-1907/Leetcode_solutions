from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if len(nums)==1:
        #     return [1]
        unique= set(nums)
        freq=defaultdict(int)
        for i in unique:
            freq[i]=nums.count(i)
        sorted_dict= dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        ans=list(sorted_dict.keys())
        return ans[0:k]