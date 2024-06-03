# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
1、先反转以 head 开头的 k 个元素。
2、将第 k + 1 个元素作为 head 递归调用 reverseKGroup 函数。
3、将上述两个过程的结果连接起来。

base case: 如果最后的元素不足 k 个，就保持不变
"""
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        a, b = head, head
        for i in range(k):
            if not b:
                return head
            b = b.next

        # 反转的区间是[a, b),也即是[a, b-1]
        newHead = self.reverse(a, b)

        # self.reverse(a, b)之后，链表从a->...->(b-1）,变成a <- ... <- (b-1)
        a.next = self.reverseKGroup(b, k)
        return newHead

    # 反转[a, b)之间的链表
    def reverse(self, a, b):
        pre, cur, nxt = None, a, a

        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # while 结束条件是cur=b，那么pre就是最后一个有效节点
        return pre