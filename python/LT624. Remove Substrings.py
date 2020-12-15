# 思路: 每个去掉substr的string都是一个子图
#      去掉一个substr的子图为第一层, 去掉两个substr的子图有第二层(如去掉ab -> ab or ab - > cd)
#      其实又变成了bfs 层搜索的感觉
#      只不过此处,在构建图的时候, 就维持了一个minLen来存储最小的len


class Solution:
    # @param {string} s a string
    # @param {set} dict a set of n substrings
    # @return {int} the minimum length
    def minLength(self, s, dict):
        # Write your code here
        queue = [s]
        has = set([s])

        minLen = len(s)
        while queue:
            s = queue.pop(0)
            for substr in dict:
                found = s.find(substr)
                while found != -1:
                    new_s = s[: found] + s[found + len(substr): ]

                    if new_s not in has:
                        queue.append(new_s)
                        has.add(new_s)

                        minLen = min(minLen, len(new_s))

                    found = s.find(substr, found + 1)
        return minLen

s = Solution()
print s.minLength("ccdaabcdbb", ["ab","cd"])