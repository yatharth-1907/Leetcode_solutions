class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums=set(range(1,n+1))
        div=[]
        for num in nums:
            if num%m==0:
                div.append(num)
        div=set(div)
        non_div= nums-div
        return sum(non_div)-sum(div)