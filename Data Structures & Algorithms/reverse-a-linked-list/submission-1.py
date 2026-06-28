# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        if curr_node == None or curr_node.next == None:
            return curr_node
        
        first = True
        while curr_node.next != None:
            next_node = curr_node.next
            if first:
                final_node = ListNode(val=curr_node.val, next=None)
                new_node = ListNode(val=next_node.val, next=final_node)
                first = False
            else:
                new_node = ListNode(val=next_node.val, next=new_node)
            curr_node, next_node = next_node, next_node.next
        return new_node