# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if head is None:
            return None

        if k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        head = dummy

        while True:
            head = self.reverse(head, k)

            if head is None:
                break
        return dummy.next

    def reverse(self, head, k):
        nk = head

        for i in range(k):
            if nk is None:
                return None
            nk = nk.next

        if nk is None:
            return None

        nkplus = nk.next

        pre = head
        cur = head.next
        nxt = cur.next

        while nxt != nkplus:
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            nxt = cur.next

        return cur

n1 = ListNode(1)
n3 = ListNode(3)
n2 = ListNode(2)
n4 = ListNode(4)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n3
n3.next = n2
n2.next = n4
n4.next = n6
n6.next = n7

s = Solution()
print s.reverseKGroup(n1, 2)