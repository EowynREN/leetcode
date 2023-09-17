# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        left, right = dummy, dummy
        for i in range(n): # right指针先走n步
            if right.next:
                right = right.next

        while right.next: # 循环结束时，left只想就是倒数第n个node的前一个node（这样可以方便删除）
            left = left.next
            right = right.next

        # delete the node
        temp = left.next
        left.next = left.next.next
        temp = None

        return dummy.next