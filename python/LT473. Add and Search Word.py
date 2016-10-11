class TrieNode:
    def __init__(self):
        self.children = {}
        self.hasWord = False


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        node = self.root
        for i in range(len(word) + 1):
            # !!!!!!!!!!!! has to add a terminal flag!!!!!!!!!!!
            # otherwise for [add, adder, addee, adds]
            # search for 'add' will return false
            # cuz when reach the 'add' end
            # the program will consider there is 'add' in the trie

            if i == len(word):
                c = '\0'  # teminate flag for the word
            else:
                c = word[i]

            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]  # move down to next level
        node.hasWord = True


    def find(self, node, index, word):
        if index == len(word):
            if '\0' in node.children:
                return True
            return False

        if word[index] in node.children:
            return self.find(node.children[word[index]], index + 1, word)
        elif word[index] == '.':
            result = False
            # for every char is ok, search the whole tree path after cur char
            # if there is  one match, return True
            # else return False
            for key in node.children.keys():
                result |= self.find(node.children[key], index + 1, word)
            return result
        else:
            return False

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.find(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


s = WordDictionary()
# print s.addWord("bad")
# print s.addWord("dad")
# print s.addWord("mad")
# print s.search("pad")
# print s.search("bad")
# print s.search(".ad")
# print s.search("b..")
s.addWord("ran")
s.addWord("rune")
s.addWord("runner")
s.addWord("runs")
s.addWord("add")
s.addWord("adds")
s.addWord("adder")
s.addWord("addee")
s.search("r.n")
s.search("ru.n.e")
s.search("add")
s.search("add.")
s.search("adde.")
s.search(".an.")
s.search("...s")
s.search("....e.")
s.search(".......")
s.search("..n.r")