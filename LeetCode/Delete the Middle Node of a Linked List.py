# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(next=head)
        first=res
        second=head
        while second and second.next:
            first=first.next
            second=second.next.next
        first.next=first.next.next
        return res.next