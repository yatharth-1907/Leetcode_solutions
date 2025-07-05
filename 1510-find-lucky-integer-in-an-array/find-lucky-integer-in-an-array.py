class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=list(set(arr))
        s.sort()
        largest=-1
        for i in s:
            if arr.count(i)==i:
                largest=max(largest,i)
        return largest

        