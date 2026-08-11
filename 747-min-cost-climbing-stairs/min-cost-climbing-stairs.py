class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[]
        n=len(cost)
        for i in range(n):
            if not dp or len(dp)==1:
                dp.append(cost[i])
                continue
            dp.append(min(dp[i-1],dp[i-2])+cost[i])
        return (min(dp[-2], dp[-1]))
