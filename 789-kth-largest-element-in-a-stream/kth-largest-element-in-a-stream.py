class KthLargest:
    l=[]
    k=0
    def __init__(self, k: int, nums: List[int]):
        KthLargest.l=nums
        KthLargest.k=k

    def add(self, val: int) -> int:
        KthLargest.l.append(val)
        l=KthLargest.l
        l.sort(reverse=True)
        return l[KthLargest.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)