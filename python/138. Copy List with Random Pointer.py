
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        originToClone = {}

        # 第一次遍历，先把所有节点克隆出来
        p = head
        while p:
            if p not in originToClone:
                originToClone[p] = Node(p.val)
            p = p.next

        # 第二次遍历，把克隆节点的结构连接好
        p = head
        while p:
            if p.next:
                originToClone[p].next = originToClone[p.next]
            if p.random:
                originToClone[p].random = originToClone[p.random]
            p = p.next

        return originToClone[head]