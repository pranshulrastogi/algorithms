'''
Problem link:https://leetcode.com/problems/reverse-linked-list/
Difficulty: Medium
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        p = head
        q = head.next
        nl = self.reverseList(q)
        q.next = p
        p.next = None
        return nl