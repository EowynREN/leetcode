#-*- coding:utf8 -*-
#coding=utf-8

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        q = ['0000']
        visited = {'0000'}
        death = set(deadends)
        depth = 0

        # BFS层遍历
        while q:
            count = len(q) # count node in the same level

            for _ in range(count):
                cur = q.pop(0)

                # 避免踩雷
                if cur in death:
                    continue

                if cur == target:
                    return depth

                # 分别拨动四个密码轮所能产生的结果
                for i in range(4):
                    up = self.plusOne(cur, i)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)

                    down = self.minusOne(cur, i)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)

            # 在这里增加层遍历的步数
            depth += 1

        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1

    def plusOne(self, password, index):
        charArr = list(password)
        if charArr[index] == '9':
            charArr[index] = '0'
        else:
            charArr[index] = str(int(charArr[index]) + 1)
        return ''.join(charArr)

    def minusOne(self, password, index):
        charArr = list(password)
        if charArr[index] == '0':
            charArr[index] = '9'
        else:
            charArr[index] = str(int(charArr[index]) - 1)
        return ''.join(charArr)


s = Solution()
print s.openLock(["0000"], "8888")