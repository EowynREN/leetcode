# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # has circle
                break

        if not fast or not fast.next:  # no circle
            return None

        slow = head  # rewind slow pointer to the start
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
