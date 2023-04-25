# 思路: http://bookshadow.com/weblog/2016/11/22/leetcode-lfu-cache/

class KeyNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class FreqNode:
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.prev = None
        self.first = None
        self.last = None


class LFUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.head = FreqNode(-1)
        self.freqList = {}
        self.keyList = {}


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # edge case
        if self.capacity == 0:
            return

        # hit cache ----> reset cache value & increase its frequence
        if key in self.keyList:
            self.keyList[key].val = value
            self.increase(self.keyList[key])
            return
        # hit miss ----> evict the least frequent used one if cache is full
        # add add the new one in
        if len(self.keyList) == self.capacity:
            self.delete_knode()
        self.insert_knode(key, value)

    # @return an integer
    def get(self, key):
        # write your code here
        if key in self.keyList:
            knode = self.keyList[key]
            self.increase(knode)
            return knode.val
        return -1

    def increase(self, knode):
        # increase freq
        fnode = self.freqList[knode.freq]
        knode.freq += 1

        new_fnode = fnode.next
        # adjust freq order in freqence linked list
        if not fnode.next or fnode.freq + 1 < fnode.next.freq:
            new_fnode = self.insert_fnode(fnode.freq + 1, fnode)

        # rearrange the knode's place
        self.unlink(knode, fnode)
        self.link(knode, new_fnode)

    def insert_fnode(self, freq, fnode):
        # insert new fnode into freqence linked list
        new_fnode = FreqNode(freq)
        new_fnode.next = fnode.next
        new_fnode.prev = fnode
        fnode.next = new_fnode
        if new_fnode.next:
           new_fnode.next.prev = new_fnode

        # add a fnode in frequence hashmap
        self.freqList[freq] = new_fnode

        return new_fnode

    def insert_knode(self, key, val):
        new_knode = KeyNode(key, val)
        self.keyList[key] = new_knode

        # fnode = self.freqList[1]
        if 1 in self.freqList:
            self.link(new_knode, self.freqList[1])
        else:
            new_fnode = self.insert_fnode(1, self.head)
            self.link(new_knode, new_fnode)

    def unlink(self, knode, fnode):
        # unlink the knode from previous frequence linked list
        if knode.prev:
            knode.prev.next = knode.next

        if knode.next:
            knode.next.prev = knode.prev

        if knode == fnode.first:
            fnode.first = knode.next

        if knode == fnode.last:
            fnode.last = knode.prev

        knode.prev = knode.next = None

        # if list on this frequence is empty, delete this frequence node
        if not fnode.first or not fnode.last:
            self.delete_fnode(fnode)

    def link(self, knode, fnode):
        # link knode in new frequence list
        # init its first and last pointer on first time
        if not fnode.first:
            fnode.first = knode

        if not fnode.last:
            fnode.last = knode
        else:
            knode.prev = fnode.last
            fnode.last.next = knode
            fnode.last = knode

    def delete_fnode(self, fnode):
        # delete from frequence list
        if fnode.prev:
            fnode.prev.next = fnode.next
        if fnode.next:
            fnode.next.prev = fnode.prev

        # delete from frequence hash map
        del self.freqList[fnode.freq]

    def delete_knode(self):
        fnode = self.head.next
        knode = fnode.first

        # unlink from frequence list
        self.unlink(knode, fnode)
        # delete from keynode hash map
        del self.keyList[knode.key]