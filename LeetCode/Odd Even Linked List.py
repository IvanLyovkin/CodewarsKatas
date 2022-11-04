# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        temp = head
        if not temp:
            return head

        first_list = head
        second_list = head.next
        save = second_list
        while first_list.next and second_list.next:
            first_list.next = second_list.next
            first_list = first_list.next
            if first_list:
                second_list.next = first_list.next
                second_list = second_list.next
        first_list.next = save
        return head