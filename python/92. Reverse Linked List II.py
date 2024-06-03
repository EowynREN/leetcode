# 这道题有iteration和recursion两种思路
# iteration版本：需要注意很多细节
# recursion版本：注意对递归函数的定义（着重想base case的意义）和返回值的定义
# 此题还有一个基础版206. Reverse Linked List (反转链表)

# recursion版本
class Solution(object):
    def __init__(self):
        self.successor = None

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

# iteration版本
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 保持pre，temp和head指针的位置不变
        # pre永远指向扭转区间的前一个node
        # temp永远指向pre后一个位置（扭转区间的第一个node）
        # head始终是初始的head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for i in range(left - 1):
            pre = pre.next
            head = head.next

        for i in range(right - left):
            temp = pre.next
            pre.next = head.next
            head.next = head.next.next
            pre.next.next = temp
        return dummy.next