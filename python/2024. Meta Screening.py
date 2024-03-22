# Write a function that returns true if a given string is a palindrome (a
# palindrome is a string that is the same when reversed, if you ignore
# punctuation and capitalization).  Some examples of palindromes are:
#   "Race car!"
#   "A man, a plan, a canal, Panama!"

def isPalindrome(s):
    if len(s) == 0:
        return True

    array_s = []
    for c in s:
        if c.isAlpha():
            array_s.append(c.lowercased())

    left, right = 0, len(array_s) - 1
    while left < right:
        if array_s[left] == array_s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# array_s = [r, a, c, e, c, a, r]
# left = 0, 1, 2, 3,
# right = 6, 5, 4, 3


# Given a starting word, an ending word, and a dictionary of valid words, return a list of words that starts and ends with the specified words and each element differs from its neighbors by exactly one letter.

# Example: start # FACE, end BOOK, dictionary = (All English Words)
# FACE
# RACE
# RACK
# ROCK
# ROOK
# BOOK


def getEditTrace(start, end, dictionary):
    # stack = [start]
    # visited = set()
    # visited.add(start)
    # trace = []

    # while stack:
    #     word = stack.pop()
    #     neighbors = getValidNeighbors(word, dictionary)
    #     for neighbor in neighbors:
    #         if neighbor == end:
    #             break

    #         if neighbor not in visited:
    #             stack.append(neighbor)
    #             visited.add(neighbor)
    #             trace.append(neighbor)
    res = []
    return dfs(start, end, dictionary, [], set(), res)


def dfs(start, end, dictionary, trace, visited, res):
    if start == end:
        res.append(list(trace))
        return

    if start in visited:
        return

    neighbors = getValidNeighbors(start, dictionary)

    visited.add(start)
    trace.append(start)
    for neighbor in neighbors:
        dfs(neighbor, end, dictionary, trace, visited, res)
    del trace[-1]


def getValidNeighbors(word, dictionary):  # list of valid neighbors
    alphabet = ["A", "B", "C", "D"]  # 26 letters
    neighbors = []
    for i in range(len(word)):
        for alpha in alphabet:
            if word != alpha:
                valid = ""
                if i == 0:
                    valid = alpha + word[i + 1:]
                elif i == len(word) - 1:
                    valid = word[i - 1:] + alpha
                else:
                    valid = word[:i - 1] + alpha + word[i + 1:]

                if valid in dictionary:
                    neighbors.append(valid)
    return neighbors



