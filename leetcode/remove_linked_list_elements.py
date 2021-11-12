"""
Problem link: https://leetcode.com/problems/remove-linked-list-elements/
Difficulty: Easy
"""


def removeElements(head, val):
    """
    :type head: datastructures.linkedlist.SingleLinkedListNode
    :type val: int
    :rtype: datastructures.linkedlist.SingleLinkedListNode
    """
    p = head
    prev = None
    while p:
        if p.val == val:
            if p == head:
                p = p.next
                head = p
            else:
                prev.next = p.next
                p = p.next
        else:
            prev = p
            p = p.next
    return head
