# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 测圈法
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur = headA
        while cur.next:
            cur = cur.next

        cur.next = headB  # link tail of A to the head of B
        node = self.detectCycle(headA)
        cur.next = None  # undo the link action
        return node

    # solution to question 142
    def detectCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:  # no circle
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# 将来那个链表首尾相接， A接B， B接A（不用真的link起来，指针调到A的头就可以），"如此长度就相等"
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1