class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre = [None]
        res = []

        self.helper(root, pre,res)
        if res:
            tmp = res[0].val
            res[0].val = res[1].val
            res[1].val = tmp

    def helper(self, root, pre, res):
        if not root:
            return

        self.helper(root.left, pre, res)

        if pre[0] and pre[0].val > root.val:
            if len(res) == 0:
                res.append(pre[0])
                res.append(root)
            else:
                res[1] = root

        pre[0] = root

        self.helper(root.right, pre, res)

s = Solution()

t0 = TreeNode(0)
t1 = TreeNode(1)
t0.left = t1

print s.recoverTree(t0)