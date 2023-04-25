
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None

        # check if there is cycle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        # find out the beginner of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

l1 = ListNode(1)
l2 = ListNode(-1)
l1.next = l2
l2.next = None
s = Solution()
print s.detectCycle(l1)