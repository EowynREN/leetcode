# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 这道题有iteration和recursion两种思路
# iteration版本：需要注意很多细节
# recursion版本：注意对递归函数的定义（着重想base case的意义）和返回值的定义
# 此题还有一个加强版92. Reverse Linked List II (给一个索引区间 [m, n]， 反转链表的这一部分)

# 迭代解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


# 递归解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果链表为空或者只有一个节点的时候，反转结果就是它自己，直接返回即可
        if not head or not head.next:
            return head

        # 当链表递归反转之后，新的头结点是 last，而之前的 head 变成了最后一个节点
        last = self.reverseList(head.next)
        head.next.next = head
        # 别忘了链表的末尾要指向 null
        head.next = None
        return last
