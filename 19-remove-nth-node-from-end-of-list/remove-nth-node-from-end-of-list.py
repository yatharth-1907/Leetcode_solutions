# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr=head
        count=0
        while itr!=None:
            itr=itr.next
            count+=1
        iter=1
        i=head
        j=i.next
        if count-n==0:
            head=head.next
        else:
            while iter<count-n:
                iter+=1
                i=i.next
                j=j.next
            i.next=j.next

        return head 
        