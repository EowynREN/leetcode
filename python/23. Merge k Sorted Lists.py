import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        if not lists:
            return None

        # push all head into min heap
        min_heap = []
        for i in range(len(lists)):  # klog(k)
            if lists[i]:
                heapq.heappush(min_heap, lists[i])

        dummy = ListNode(0)
        cur = dummy
        while min_heap:  # nlog(k), each node will added into heap and popped once
            node = heapq.heappop(min_heap)

            if node.next:
                heapq.heappush(min_heap, node.next)

            cur.next = node
            cur = cur.next

        cur.next = None
        return dummy.next


