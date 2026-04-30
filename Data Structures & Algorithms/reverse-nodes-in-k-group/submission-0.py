# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def hasknodes(node,k):
            current= node
            count=0
            while current and count<k:
                count+=1
                current=current.next
            
            return count==k
        
        def reverseknodes(head,k):
            current=head
            prev=None
            for i in range(k):
                nextnode= current.next
                current.next=prev
                prev= current
                current= nextnode
            return prev, current

        dummy= ListNode(0)
        dummy.next= head
        prevgroup= dummy

        while hasknodes(prevgroup.next,k):
            groupstart= prevgroup.next
            newgrouphead, nextgroupstart= reverseknodes(groupstart,k)

            prevgroup.next= newgrouphead
            groupstart.next= nextgroupstart
            prevgroup= groupstart

        return dummy.next
