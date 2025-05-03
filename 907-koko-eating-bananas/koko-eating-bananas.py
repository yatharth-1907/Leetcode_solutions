class Solution:

    #main fuction
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower=1
        upper=max(piles)
        while (upper>=lower):
            mid= math.ceil((lower+upper)/2)
            valid= self.cal_hour(piles, mid)
            if(valid<= h):
                upper= mid-1
            
            else:
                lower= mid+1
        
        return lower

    def cal_hour(self,piles:list[int], rate:int)->int:
        hour=0
        for pile in piles:
            hour= hour+ math.ceil(pile/rate)

        return hour


    