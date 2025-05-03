class Solution:
    def climbStairs(self, n: int) -> int:
        #  to get the previous two values.
        prev1,prev2=1,1
        for i in range(1,n):
            sum=prev1+prev2
            prev2=prev1
            prev1=sum

        return prev1