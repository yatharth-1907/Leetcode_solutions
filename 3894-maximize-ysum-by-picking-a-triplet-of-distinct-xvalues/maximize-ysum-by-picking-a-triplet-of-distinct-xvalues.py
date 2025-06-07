class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hashmap= defaultdict(list)
        maximum=[]
        for i in range(len(x)):
            hashmap[x[i]].append(y[i])
        if(len(hashmap)<3):
            return -1
        else:
            for key in hashmap:
                maximum.append(max(hashmap[key]))
        maximum= sorted(maximum,reverse=True)
        return(maximum[0]+maximum[1]+maximum[2])