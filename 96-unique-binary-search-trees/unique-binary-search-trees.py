class Solution:
    def numTrees(self, n: int) -> int:
        numtrees=[1]*(n+1)

        for node in range(2, n+1):
            total=0
            for i in range(1,node+1):
                left= i-1
                right= node- i
                total+= numtrees[left]*numtrees[right]
            numtrees[node]= total
        return numtrees[n]