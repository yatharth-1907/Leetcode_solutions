class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)-1
        swaps=0
        # element= s.count('1')-1
        
        for i in range(n,-1,-1):
            if s[i]=='1':
                swaps=swaps+n-i
                n-=1
        return swaps
