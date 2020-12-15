class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """

    # 思路: 维持一个单调递减的队列,保持队列的大小为k
    #      首先,先把前k - 1个数压入队列
    #      当第k个数进来的时候,因为保持的单调递减队列, 队列前的数一定是最大值
    #      每pop处一个数就压入一个数
    #      但是因为在压入的时候为了保持单调递减,这个数有可能被丢弃
    #      因此在pop的时候要检查当前pop的值在不在队列中
    #      如果在,那么一定是第一个数(因为入一个出一个), 如果不在那一定是被提前丢弃了, 那么久不用pop了
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []

        res = []
        deque = []
        for i in range(k - 1):
            self.enqueue(deque, nums[i])

        for i in range(k - 1, len(nums)):
            self.enqueue(deque, nums[i])
            res.append(deque[0])
            # pop nums[i - (k - 1)] 保持队列的大小为k
            self.dequeue(deque, nums[i - k + 1])
        return res

    def enqueue(self, deque, num):
        # mantain an queue with non-increasing order
        while deque and deque[-1] < num:
            deque.pop()
        deque.append(num)

    def dequeue(self, deque, num):
        # if num is already pop up, do nothing
        # else pop it
        if deque[0] == num:
            deque.pop(0)