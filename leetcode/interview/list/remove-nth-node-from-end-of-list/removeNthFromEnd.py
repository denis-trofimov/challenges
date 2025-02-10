# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
# Your runtime beats 69.91 % of python3 submissions.
# Your memory usage beats 91.81 % of python3 submissions.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        i = 1
 
        while i <= n and node is not None and node.next is not None:
            node = node.next
            i += 1
        
        prev = head
        while node is not None and node.next is not None:
            i += 1
            node = node.next
            prev = prev.next
        
        # remove previous head
        if n == i:
            if i == 1:
                return None
            return head.next
        
        # remove the next from previous pointer, which is Nth from the end.
        prev.next = (prev.next).next
        return head