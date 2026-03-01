# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        itr=head
        l=[]

        while itr!=None:
            l.append(itr.val)
            itr=itr.next
        return True if l==l[::-1] else False