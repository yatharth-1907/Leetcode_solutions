class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_1(n):
            count=0
            while n!=0 and n!=1:
                if n%2==1:
                    count+=1
                n=n//2
            if n==1:
                count+=1
            return count
        res=[]
        for i in range(n+1):
            res.append(count_1(i))
        return res
                
        
            