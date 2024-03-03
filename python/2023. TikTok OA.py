# Q3
#
# SELECT
#     p.name,
#     p.price,
#     SUM(po.quantity) AS quantity,
#     SUM(po.quantity * p.price) AS total_price
# FROM
#     products AS p
# JOIN
#     products_orders AS po ON p.id = po.product_id
# JOIN
#     orders AS o ON po.order_id = o.id
# WHERE
#     o.status = 'Completed'
# GROUP BY
#     p.name, p.price
# ORDER BY
#     quantity DESC, total_price DESC;

class Solution(object):
    # Q4
    def getChannelRating(self, views):
        # e.g., [a, b, c, d, e]
        # 根据题干: a ^ e = b ^ c ^ d
        # 两边同乘a^e  =>  (a ^ e ) ^ (a ^ e ) = (a ^ e ) ^ b ^ c ^ d
        # 同一个数XOR自己，得到0， 所以  =>  0 = a ^ b ^ c ^ d ^ e
        # prefix[j] = prefix[i]，表明i + 1, i + 2, ..., j的XOR sum是0
        # count{XOR value: count}

        MOD = 10 ** 9 + 7

        if len(views) < 3:
            return -1

        prefix = [0] * (len(views) + 1)
        count = {0: 1}
        res = 0
        for i in range(1, len(views) + 1):
            prefix[i] = prefix[i - 1] ^ views[i - 1]

            if prefix[i] in count:
                res += count[prefix[i]]  # add all qualified subarray which ending at i
                count[prefix[i]] += 1
            else:
                count[prefix[i]] = 1

        for i in range(len(views)):
            # remove subarray with 1 item whose value is 0
            if views[i] == 0:
                res -= 1
            # remove subarray with 2 items whose value are same
            if i > 0 and views[i] == views[i - 1]:
                res -= 1
        return res % MOD

    # Q5
    def minimumCommonInteger(self, data):
        farthest = [0] * (2 * 10 ** 5 + 1)
        res = [0] * (2 * 10 ** 5 + 1)
        n = len(data)

        self.maxDistance(data, farthest, n)

        for i in range(1, n + 1):
            res[i] = -1

        for i in range(1, n + 1):

            # Check if subarray of length
            # farthest[i] contains i as one
            # of the common elements
            if res[farthest[i]] == -1:
                res[farthest[i]] = i

        for i in range(2, n + 1):

            # Find the minimum of all
            # common elements
            if res[i - 1] != -1:
                if res[i] == -1:
                    res[i] = res[i - 1]
                else:
                    res[i] = min(res[i], res[i - 1])
        return res[1: n + 1]



    def maxDistance(self, data, farthest, n):
        for i in range(1, n + 1):
            farthest[i] = -1

        itemLastIndex = {}
        for i in range(n):
            if data[i] not in itemLastIndex:
                farthest[data[i]] = i + 1
            else:
                farthest[data[i]] = max(farthest[data[i]], i - itemLastIndex[data[i]])
            itemLastIndex[data[i]] = i

        for i in range(1, n + 1):

            # Compare farthest[i] with
            # distance of its last
            # occurrence from the end
            # of the array and store
            # the maximum
            if farthest[i] != -1:
                farthest[i] = max(farthest[i], n - itemLastIndex[i])





s = Solution()
print(s.getChannelRating([4, 3, 3, 4, 2, 6, 8, 2, 0, 9])) #0, 3, 6, 5, 4, 4, 0
print(s.minimumCommonInteger([5, 2, 4, 2, 3, 5]))





