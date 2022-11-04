# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        prev = item = ListNode(0)
        prev.next = head
        while item.next:
            if item.next.val == val:
                item.next = item.next.next
            else:
                item = item.next
        return prev.next