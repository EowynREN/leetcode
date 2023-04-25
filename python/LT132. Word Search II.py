class TrieNode:
    def __init__(self):
        self.subtree = {}
        self.isEnd = False
        self.strval = ""
        # 在每一个string的最后一个node上,赋值整个string的val,不用重新遍历就得到整个string

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for i in range(len(s)):
            if s[i] not in node.subtree:
                node.subtree[s[i]] = TrieNode()
            node = node.subtree[s[i]]  # move down to next level

        node.isEnd = True
        node.strval = s

    # isn't used in this problem
    def find(self, index, word):
        node = self.root

        for c in word:
            if c not in node.subtree:
                return False
            node = node.subtree[c]
        return node.isEnd


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return False

        # 此处把字典words构造成trie树
        tt = TrieTree()
        for word in words:
            tt.insert(word)

        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 如果当前字符不是任何一个单词的开头,cut this path
                if board[i][j] not in tt.root.subtree:
                    continue
                self.search(i, j, tt.root, board, res)
        return res

    def search(self, i, j, node, board, res):
        # 如果当前node是一个string的end
        # 程序运行到这里,表示这个string里的每一个字符都是valid path(通过上下左右连接, 并且在字典中)
        # 否则在之前就会被""超出边界""或者""当前字符不在任何单词的前缀中""这两个条件给cut掉(return)
        if node.isEnd:
            if node.strval not in res:
                res.add(node.strval)

        # ----------------------边界条件-------------------------      ----当前字符不在任何单词的前缀中---
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.subtree:
            return

        # 此处'#'避免重负扫描 ----> 环路
        tmp = board[i][j]
        board[i][j] = '#'
        for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.search(i + k[0], j + k[1], node.subtree[tmp], board, res)
        # 这个字符用完后,要把原来的值返还给它
        # 之后的扫描中,其他path可能要经过这里
        board[i][j] = tmp

s = Solution()
print s.wordSearchII([['a', 'b', 'c', 'e'],['s', 'f', 'c', 's'],['a', 'd', 'e', 'e']],
                     ["as","ab","cf","da","ee","e","adee","eeda"])



