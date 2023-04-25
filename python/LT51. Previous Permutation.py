# 思路: eg: 1 2  1 2 3 4

#      1. 首先我们找到从尾部到头部第一个上升的digit. 在例子中是：2

#      2. 把从右到左第一个比dropindex小的元素换过来。

#      3. 把dropindex右边的的序列反序

#      4. 如果1步找不到这个index ，则不需要执行第二步。

# Next Permutation这道题思路一样, 大于小于号改一下即可

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        # write your code here
        n = len(num)

        for i in range(n - 2, -1, -1):
            # 刚被换过的地方
            if num[i] > num[i + 1]:
                index = 0
                for j in range(n - 1, i, -1):
                    if num[j] < num[i]:
                        index = j
                        break

                num[i], num[index] = num[index], num[i]
                self.reverse(num, i + 1, n - 1)
                return num

        self.reverse(num, 0, n - 1)
        return num


    def reverse(self, num, start, end):
        while start < end:
            num[start], num[end] = num[end], num[start]
            start += 1
            end -= 1

s = Solution()
print s.previousPermuation([1,2,1])