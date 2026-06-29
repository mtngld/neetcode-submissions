# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        curr_new = None
        prev_new = None

        if a is None:
            return b
        if b is None:
            return a

        while a and b:
            if a.val < b.val:
                curr_new = ListNode(val=a.val, next = None)
                a = a.next
            else:
                curr_new = ListNode(val=b.val, next = None)
                b = b.next
            if prev_new:
                prev_new.next = curr_new
            else: 
                new_head = curr_new
            


            prev_new = curr_new
        
        if a is not None:
            curr_new.next = a
        
        if b is not None:
            curr_new.next = b

        return new_head
        
            
        