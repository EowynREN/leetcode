"""
Definition of ExpressionTreeNode:
"""
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
import sys


class TreeNodes:
    def __init__(self, weight, s):
        self.weight = weight
        self.eNode = ExpressionTreeNode(s)


class Solution:
    # @param expression: A string list
    # @return: The root of expression tree
    def build(self, expression):
        # write your code here
        if not expression:
            return None

        stack = []
        base, weight = 0, 0
        for i in range(len(expression)):

            # 不要把括号(, )加入到tree里面，它们只改变优先级
            if expression[i] == "(":
                base += 10
                continue

            if expression[i] == ")":
                base -= 10
                continue

            # -------------- min tree ------------ #
            weight = self.getWeight(base, expression[i])
            newNode = TreeNodes(weight, expression[i])

            while stack and stack[-1].weight >= newNode.weight:
                newNode.eNode.left = stack.pop().eNode

            if stack:
                stack[-1].eNode.right = newNode.eNode

            stack.append(newNode)
            # ------------------------------------ #

        # special case : ["(","(","(","(","(",")",")",")",")",")"]
        if not stack:
            return None

        return stack[0].eNode

    def getWeight(self, base, s):
        if s == "+" or s == "-":
            return base + 1

        if s == "*" or s == "/":
            return base + 2

        return sys.maxint