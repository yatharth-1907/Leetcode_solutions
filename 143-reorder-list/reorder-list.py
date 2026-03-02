# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count =0
        itr1=head
        stack=[]

        while itr1!=None:
            count+=1
            stack.append(itr1)
            itr1=itr1.next
            
        count=(count+1)//2
        itr1=head

        for _ in range(count):
            stack.pop(0)
        
        itr1= head
        itr2=itr1.next
        while stack:
            itr1.next= stack.pop()
            itr1.next.next= itr2
            itr1=itr2
            itr2=itr2.next 

        itr1.next=None
