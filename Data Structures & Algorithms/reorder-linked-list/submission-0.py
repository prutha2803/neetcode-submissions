# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow= head
        fast= head.next

        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        
        second= slow.next
        slow.next= None

        curr= second
        prev2=None

        while curr:
            nexttemp= curr.next
            curr.next= prev2
            prev2= curr
            curr=nexttemp

        #merge
        l1= head
        l2= prev2

        while l2: #cause l2 is smaller:
            temp1= l1.next
            temp2= l2.next

            l1.next= l2
            l2.next= temp1

            l1= temp1
            l2=temp2


        

        