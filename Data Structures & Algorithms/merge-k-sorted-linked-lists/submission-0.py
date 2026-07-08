# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []
        heapq.heapify(data)
        for idx in range(len((lists))):
            heapq.heappush(data, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
        
        prev_node = None
        new_root = None
        while True:
            try:
                new_val, list_idx = heapq.heappop(data)
                new_node = ListNode(val=new_val)
                
                if prev_node is not None:
                    prev_node.next = new_node
                else:
                    new_root = new_node
                
                prev_node = new_node
                
                if lists[list_idx] is not None:
                    heapq.heappush(data, (lists[list_idx].val, list_idx))
                    lists[list_idx] = lists[list_idx].next
            
            except IndexError:
                break
        return new_root
        