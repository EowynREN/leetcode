# 思路:
#   0 的机器骂（原码）：0|0000000000000000000000000000000
#   -1的机器码（补码）：1|1111111111111111111111111111111
# 所以对0取反得到-1(由补码转换的得到的原码)

# 此题的主要思路是要算出mask:保留j ~ i(左到右)位置之外的bit,然后再把m放到j ~ i位置之中

class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        # 在对0取反后,会等到(除符号位意外)一串1(共31个)
        max = ~0

        # 把j为之后的最大值算出来(即从j位之后全是1)
        if j == 31:
            j = max
        else:
            j = (1 << (j + 1)) - 1

        # 31个1减掉j位之后的一串1,得到左半部分的mask(从最左到j位)
        left = max - j
        # 算出i位之后最大的数(即i位之后全是1), 得到右半部分的掩码
        right = ((1 << i) - 1)
        # 这时的mask除了j ~ i(包括j, i)这段区间的数为0,其他位置上全为1
        mask = left | right

        # (n & mask) ----> n这个数j ~ i的位置空了出来
        # (m << i) ----> 把m这个数推到合适的位置(落在j ~ i 的区间里)
        # |操作 ---> 把m放到n的j~i位置上
        return ((n & mask) | (m << i))

s = Solution()
print s.updateBits(35, 41, 3, 6)