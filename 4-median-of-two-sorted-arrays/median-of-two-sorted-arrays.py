class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=nums1+nums2
        merge=sorted(merge)
        size=len(merge)
        mid=size//2
        if size%2==0:
            return((merge[mid-1]+merge[mid])/2)
        else:
            return(merge[mid])
