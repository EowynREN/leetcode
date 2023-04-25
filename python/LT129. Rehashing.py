
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        n = len(hashTable)
        res = [None] * 2 * n

        for i in range(n):
            while hashTable[i]:
                index = hashTable[i].val % (2 * n)
                if res[index]:
                    dummy = res[index]
                    while dummy.next:
                        dummy = dummy.next
                    dummy.next = ListNode(hashTable[i].val)
                else:
                    res[index] = ListNode(hashTable[i].val)

                hashTable[i] = hashTable[i].next
        return res

s = Solution()
l1 = ListNode(80)
l2 = ListNode(187)
l3 = ListNode(49)
l4 = ListNode(109)
l3.next = l4
l5 = ListNode(10)
l6 = ListNode(50)
l7 = ListNode(-10)
l5.next = l6
l6.next = l7
l8 = ListNode(12)
l9 = ListNode(53)
l10 = ListNode(133)
l11 = ListNode(153)
l12 = ListNode(93)
l9.next = l10
l10.next = l11
l11.next = l12
l13 = ListNode(15)
l14 = ListNode(36)
l15 = ListNode(-3)
l16 = ListNode(118)
l17 = ListNode(159)
l18 = ListNode(139)
l17.next = l18

print s.rehashing([l1,None,None,None,None,None,None,l2,None,l3,l5,None,l8,l9,None,l13,l14,l15,l16,l17])