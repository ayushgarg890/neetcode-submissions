# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node=node
    
    def __lt__(self, other):
        return self.node.val< other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        res = ListNode(0)
        cur = res
        minHp=[]

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHp, NodeWrapper(lst))
            
        while minHp:
            node_wp = heapq.heappop(minHp)
            cur.next = node_wp.node
            cur=cur.next

            if node_wp.node.next:
                heapq.heappush(minHp, NodeWrapper(node_wp.node.next))

        return res.next
        