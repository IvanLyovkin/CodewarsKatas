# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        item = node.next
        while item.next:
            node.val = item.val
            node = node.next
            item = item.next
        node.val = item.val
        node.next = None