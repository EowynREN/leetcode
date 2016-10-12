class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if not board:
            return False

        res = False
        # 此处的两层for循环,是为了找到word的第一个单词的位置在哪里
        for i in range(len(board)):
            for j in range(len(board[0])):
                # cut掉不必要的search, search函数的cost很高
                if board[i][j] != word[0]:
                    continue
                res |= self.search(i, j, 0, word, board)

            # 只要有一天路径为true(即,查找到了word),就直接返回
            if res:
                return res
        return res

    def search(self, i, j, index, word, board):
        # 多递归一层, 如果能递归到第n层,说明前面0->n - 1层都未返回false
        #                                              (即每个word里的字符都在board找到了合法的路径 --- 上下左右)
        # 证明word已经找到, 返回true
        if index == len(word):
            return True

        # 检查边界条件
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False

        res = False
        # marked as visited
        # 避免递归backtrack的时候扫描已经在res路径上的字符,避免环路
        # 此处不需要多开一个visited 2-d数组,可以直接用board
        board[i][j] = '#'
        for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            res |= self.search(i + k[0], j + k[1], index + 1, word, board)

        # !!此处注意!!
        # 当执行到这一步的时候,说明当前位置(i, j)的上下左右已经被遍历递归完了
        # 此时,整个程序都在返回它上一层的栈
        # 如果当前这个字符在res的路径上,也就是res为true时(证明已查找到word)
        # board[i][j]不可以被给予原来的值,而应该保持'#' (即:这个点不可被扫描到)
        # 这样做可以避免在返回上层栈的时候,for循环再次去访问这个位置 ----> 节省时间
        # 因为已经找到word了,不需要再去做多余的查找
        # again!! search函数的递归cost很高

        # 如果res为false,证明通过这个字符的路径与word不match
        # 因此需要把它原来的值返还给它
        # 表示:这个位置还可以被扫描到
        if not res:
            board[i][j] = word[index]
        return res


s = Solution()
print s.exist(["ABCE","SFES","ADEE"], "ABCESEEEFS")