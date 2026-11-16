# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    
    def mergeTwoLists(self, list1: List[ListNode], list2: List[ListNode])->List[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        while(len(lists)>1): #master loop which stops when the lists become unified
            merged_lists = []
            for i in range(0, len(lists), 2): # pair wise step increment
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None #avoiding out of bounds access
                if l2 is  None or l2== []: # if one sub-lists does not exist or is empty
                    merged_lists.append(self.mergeTwoLists(l1, None))
                else:
                    merged_lists.append(self.mergeTwoLists(l1, l2))    
            lists = merged_lists
    
        return lists[0]
