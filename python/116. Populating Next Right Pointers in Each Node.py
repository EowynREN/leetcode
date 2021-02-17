#-*- coding:utf8 -*-
#coding=utf-8

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            self.connectTwoNodes(root.left, root.right)
        return root
    
    def connectTwoNodes(self, node1, node2):
        if not node1 or not node2:
            return

        # 前序遍历
        # connect current two nodes
        node1.next = node2
        
        # connect sub tree's left node and right node
        self.connectTwoNodes(node1.left, node1.right)

        # 中序遍历也是可以的, 前序/中序/后序取其一即可
        # connect current two nodes
        # node1.next = node2

        self.connectTwoNodes(node2.left, node2.right)
        
        # connect two adjacent nodes span two sub trees
        self.connectTwoNodes(node1.right, node2.left)

        # 后序遍历也是可以的,前序/中序/后序取其一即可
        # connect current two nodes
        # node1.next = node2