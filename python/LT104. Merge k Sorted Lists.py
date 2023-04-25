import heapq


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists or len(lists) == 0:
            return None

        k = len(lists)
        dummy = ListNode(-1)
        heap = []

        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))

        dummy = ListNode(-1)
        tail = dummy
        while heap:
            node = heapq.heappop(heap)[1]
            tail.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            tail = tail.next
        return dummy.next

n1 = ListNode(2)
n1.next = None
n2 = ListNode(-1)
n2.next = None

s = Solution()
print s.mergeKLists([n1, None, n2])
