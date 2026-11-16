# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        # find the mid
        i=0
        while curr:
           i+=1
           curr = curr.next
        mid = (i-1)//2 
        # reverse the 2nd half
        prev = None
        curr = head
        i =0
        second = None
        ## walk till mid
        while i!=mid:
            curr = curr.next # tail of the first half
            i+=1
        
        # break the next connection from mid.
        second = curr.next # moves to the head of the second half
        curr.next = None

        # reverse this list.
        while second is not None:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node 
        
        # prev is now the second half's head  node
        ## re-naming the variables
        even = head
        odd = prev
        # stich both halves in inter-leaved fashion
        i = 0
        while even and odd:
            temp1 = even.next
            temp2 = odd.next
            
            even.next = odd
            odd.next = temp1
            even = temp1
            odd = temp2



            