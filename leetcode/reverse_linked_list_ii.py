'''
Problem link: https://leetcode.com/problems/reverse-linked-list-ii/
Difficulty: medium

Problem stmt:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
                
                
            
        ll = []
        rl = []
        st = []
        p=head
        i=1
        while i<left and p:
            ll.append(p.val)
            p=p.next
            i+=1
        while i<=right and p:
            st.append(p.val)
            i+=1
            p=p.next
        while p:
            rl.append(p.val)
            p=p.next
        print(f"ll: {ll}, st: {st}, RL: {rl}")
        
        i=1
        p = None
        new_head = None
        ll = ll[::-1]
        while ll:
            val = ll.pop()
            # print(f"adding {val}")
            if not p:
                p = ListNode(val)
                new_head = p
            else:
                p.next = ListNode(val)
                p = p.next
        while st:
            val = st.pop()
            # print(f"adding {val}")
            if not p:
                p = ListNode(val)
                new_head=p
            else:
                node = ListNode(val=val)
                p.next = node
                p=p.next
            i+=1
        rl = rl[::-1]
        while rl:
            val = rl.pop()
            # print(f"adding {val}")
            if not p:
                p = ListNode(val)
                new_head = p
            else:
                node = ListNode(val=val)
                p.next = node
                p=p.next
        p = new_head
        while p:
            print(f"{p.val}", end="--")
            p=p.next
        return new_head
