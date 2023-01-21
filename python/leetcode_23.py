from typing import *
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node is not None:
                heapq.heappush(heap, node.val)
                node = node.next
        result = curr = ListNode()
        while heap:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
        return result.next