# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object): # 快慢指针
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head

        while fast and fast.next: # 注意这里，fast指针要走两步，所以fast.next也要验证
            slow = slow.next
            fast = fast.next.next

        return slow