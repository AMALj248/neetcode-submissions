# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i=0
        while curr:
            i+=1
            curr = curr.next
        N = i
        i=0
        curr = head
        while curr:
            if n ==N:
                return head.next
            if i == N-n-1:
                # deleting the link
                curr.next  = curr.next.next
            curr = curr.next
            i+=1
        return head
