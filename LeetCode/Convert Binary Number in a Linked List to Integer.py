# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
     def getDecimalValue(self, head):
         N = ""
         while head: 
             N += str(head.val)
             head = head.next 
         return int(N, 2)