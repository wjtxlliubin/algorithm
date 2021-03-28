# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 :
            return l2

        if not l2 :
            return l1

        if l1.val < l2.val :
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else :
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    lnode1 = [ListNode(i) for i in l1]
    lnode2 = [ListNode(i) for i in l2]
    l1_len = 0
    l2_len = 0

    while l1_len + 1  < len(lnode1):
        lnode1[l1_len].next = lnode1[l1_len+1]
        l1_len+=1

    while l2_len + 1  < len(lnode2):
        lnode2[l2_len].next = lnode2[l2_len+1]
        l2_len += 1

    result = Solution().mergeTwoLists(lnode1[0],lnode2[0])

    next = result
    while next.next:
        print(next.val)
        next = next.next
