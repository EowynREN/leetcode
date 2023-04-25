class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def serialize(self, root):
        # write your code here
        res = '{'
        queue = [root]
        while queue:
            node = queue.pop(0)

            if node:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += '#'
            res += ','

        # 这里是处理在叶子节点的左右孩子(都是none), 所以没必要保存(占用空间)
        for i in range(len(res) - 1, -1, -1):
            if res[i] not in ['#', ',']:
                res = res[: i + 1]
                break

        res += '}'

        return res

    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None

        data = data[1: -1].split(',')

        # first get all tree nodes
        nodes = []
        for i in range(len(data)):
            if data[i] == '#':
                node = None
            else:
                node = TreeNode(int(data[i]))
            nodes.append(node)

        # 这两个变量很重要
        # index指向当前这个node的parent的位置
        # isLeftChild决定当前node是index指向的paernt的左孩子还是右孩子
        # 因为二叉树,不是左孩子,就是右孩子
        index = 0
        isLeftChild = True
        for i in range(1, len(nodes)):
            node = nodes[i]

            # 如果有当前的节点是none的话,就跳过(这个节点不应该有左右孩子)
            while not nodes[index]:
                index += 1

            if node:
                if isLeftChild:
                    nodes[index].left = node
                else:
                    nodes[index].right = node

            if not isLeftChild:
                index += 1

            # 赋值了左孩子以后, 需要下个节点要被赋值到右孩子处
            isLeftChild = not isLeftChild
        return nodes[0]


s = Solution()
root = s.deserialize('{1,2,#,3,#,4}')
print s.serialize(root)