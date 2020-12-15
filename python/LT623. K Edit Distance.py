class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
        self.s = ""


class Trie:
    def __init__(self):
        self.root = TrieNode(" ")

    def insert(self, word):
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                new_node = TrieNode(c)
                cur.children[c] = new_node
                cur = new_node
        cur.isWord = True
        cur.s = word


class Solution:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements
    def kDistance(self, words, target, k):
        # Write your code here
        trie = Trie()
        for word in words:
            trie.insert(word)

        dp = [i for i in range(len(target) + 1)]

        res = []
        self.find(target, k, dp, trie.root, res)
        return res

    def find(self, target, k, dp, node, res):
        n = len(target)
        if node.isWord and dp[n] <= k:
            res.append(node.s)

        next = [0 for i in range(n + 1)]
        for c in node.children:
            next[0] = dp[0] + 1
            for j in range(1, n + 1):
                if c == target[j - 1]:
                    next[j] = min(dp[j - 1], min(next[j - 1] + 1, dp[j] + 1))
                else:
                    next[j] = min(dp[j - 1] + 1, min(next[j - 1] + 1, dp[j] + 1))

            self.find(target, k, next, node.children[c], res)