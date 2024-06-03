import sys

class Solution:

    def verticalOrder(self, root):
        if not root:
            return None

        queue = [(0, root)]  # (vertical order label, node)
        orderToNodes = {0, [root]}
        min_order = sys.maxsize
        max_order = -sys.maxsize - 1

        # get order to nodes map
        while queue:
            order, node = queue.pop(0)

            if order in orderToNodes:
                orderToNodes[order].append(node)
            else:
                orderToNodes[order] = [node]

            if node.left:
                queue.append((order - 1, node.left))

            if node.right:
                queue.append((order + 1, node.right))

            min_order = min(min_order, order)
            max_order = max(max_order, order)

        res = []
        for i in range(min_order, max_order + 1):
            if i in orderToNodes:
                res.append(orderToNodes[i])
        return res