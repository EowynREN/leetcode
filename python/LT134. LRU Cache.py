# 思路: LRU，也就是least recently used，最近使用最少的；
#      这样一个数据结构，能够保持一定的顺序，使得最近使用过的时间或者顺序被记录
#      实际上，具体每一个item最近一次何时被使用的，并不重要，重要的是在这样的一个结构中，item的相对位置代表了最近使用的顺序

#      ----> 满足这样考虑的结构可以是链表list或者数组array，
#      ----> 不过前者更有利于insert和delete的操纵
#      ----> 此外，需要记录这个链表的head和tail，方便进行移动到tail或者删除head的操作，
#            即：head.next作为最近最少使用的item，tail.prev为最近使用过的item，
#      ----> 在set时，如果超出capacity，则删除head.next，同时将要插入的item放入tail.prev,
#      ---->  而get时，如果存在，只需把item更新到tail.prev即可。
# 这样set与get均为O(1)时间的操作 （HashMap Get/Set + LinkedList Insert/Delete)，空间复杂度为O(n), n为capacity。

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity

        self.hashMap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.hashMap:
            return -1

        # lose both its link
        cur = self.hashMap[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        self.move_to_tail(cur)

        return self.hashMap[key].val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if self.get(key) != -1:
            self.hashMap[key].val = value
            return

        if len(self.hashMap) == self.capacity:
            del self.hashMap[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        insert = Node(key, value)
        self.hashMap[key] = insert
        self.move_to_tail(insert)


    def move_to_tail(self, cur):
        cur.next = self.tail
        cur.prev = self.tail.prev
        self.tail.prev.next = cur
        self.tail.prev = cur
