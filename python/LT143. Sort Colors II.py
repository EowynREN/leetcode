class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        count_arr = [0] * (k + 1)

        for i in range(len(colors)):
            count_arr[colors[i]] += 1

        index = 0
        for i in range(len(count_arr)):
            count = count_arr[i]
            for j in range(count):
                colors[index] = i
                index += 1
        return colors

s =Solution()
print s.sortColors2([3,2,2,1,4], 4)