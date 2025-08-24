class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd= n*n
        sumEven= n*(n+1)

        smaller= sumOdd if sumOdd<sumEven else sumEven
        larger= sumOdd if sumOdd>sumEven else sumEven
        ans=0

        while smaller!=0:
            ans=smaller
            smaller= larger%smaller
        return ans