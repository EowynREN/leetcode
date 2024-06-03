class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer

    # dfs带权求和
    # 把stack换成queue，就是bfs带权求和，写法一摸一样
    def depthSum(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0

        stack = []
        sum = 0
        for item in nestedList:
            stack.append((item, 1))

        while stack:
            item, d = stack.pop(0)
            if item.isInteger():
               sum += d * item.getInteger()
            else:
                for i in item.getList():
                    stack.append((i, d+1))
        return sum