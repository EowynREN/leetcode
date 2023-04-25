class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isPrefixOf = []


class Trie:
    def __init__(self, words):
        self.root = TrieNode(' ')

        for word in words:
            cur = self.root

            for c in word:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    newNode = TrieNode(c)
                    cur.children[c] = newNode
                    cur = newNode

                cur.isPrefixOf.append(word)

    def findByPrefix(self, prefix):
        res = []
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return []

            cur = cur.children[c]

        res += cur.isPrefixOf

        return res


class Solution:
    # @param {string[]} words a set of words without duplicates
    # @return {string[][]} all word squares

    def __init__(self):
        self.squares = []
        self.square = []
        self.trie = None
        self.length = 0

    def wordSquares(self, words):
        # Write your code here
        if not words:
            return []

        self.trie = Trie(words)
        self.length = len(words)

        for word in words:
            self.square.append(word)
            self.dfs(1)
            del self.square[-1]

        return self.squares

    def dfs(self, index):
        if index == self.length:
            self.squares.append(list(self.square))
            return

        prefix = ""
        for line in self.square:
            prefix += line[index]

        candidates = self.trie.findByPrefix(prefix)
        for candidate in candidates:
            self.square.append(candidate)
            self.dfs(index + 1)
            del self.square[-1]

s = Solution()

print s.wordSquares(["area","lead","wall","lady","ball"])