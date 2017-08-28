"""
Definition of ExpressionTreeNode:
"""
import sys

class ExpressionTreeNodes:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None


class TreeNodes:
    def __init__(self, weight, s):
        self.weight = weight
        self.eNode = ExpressionTreeNodes(s)

# LT367: Expression Tree Build
class ExpressionTreeBuild:
    # @param expression: A string list
    # @return: The root of expression tree
    def build(self, expression):
        # write your code here
        if not expression:
            return None

        stack = []
        base, weight = 0, 0
        for i in range(len(expression)):


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


class Solution:
    """
    @param: expression: a list of strings
    @return: an integer
    """
    def evaluateExpression(self, expression):
        # write your code
        et = ExpressionTreeBuild()

        # 逆波兰
        root = et.build(expression)

        stack = self.postOrderTraversal(root, [])

        return stack[0] if stack else 0

    def postOrderTraversal(self, node, stack):
        if not node:
            return stack

        self.postOrderTraversal(node.left, stack)
        self.postOrderTraversal(node.right, stack)

        if node.symbol.isdigit():
            stack.append(int(node.symbol))
        else:
            second = stack.pop()
            first = stack.pop()

            if node.symbol == "+":
                stack.append(first + second)
            elif node.symbol == "-":
                stack.append(first - second)
            elif node.symbol == "*":
                stack.append(first * second)
            else:
                stack.append(first / second)

        return stack


s = Solution()
print s.evaluateExpression(["2", "*", "6", "-", "(","23", "+", "7", ")", "/","(", "1", "+", "2", ")"])