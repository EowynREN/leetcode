
class Solution(object):
    # Time: O(n)
    # Space: O(n)
    def lowestCommonAncestor(self, p, q):
        """
        :type a: Node
              b: Node
        :rtype: Node
        """
        ancestors = set()

        a = p
        while a:
            ancestors.add(a)
            a = a.parent

        b = q
        while b:
            if b in ancestors:
                return b
            b = b.parent
        return None

    # Time: O(n)
    # Space: O(1)
    def lowestCommonAncestor2(self, p, q):
        """
        :type a: Node
              b: Node
        :rtype: Node
        """
        """
        这个解法已经不是递归树的思想了，而是求两条链表的intersection
        """
        a, b = p, q

        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p

        return a