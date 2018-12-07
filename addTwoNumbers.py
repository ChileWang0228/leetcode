#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-24 14:05
@Author:ChileWang
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            carry = 0
            ret_Last = ListNode(-1)
            cur = ret_Last
            while (l1 or l2):
                sum = 0
                if (l1):
                    sum = l1.val
                    l1 = l1.next
                if (l2):
                    sum += l2.val
                    l2 = l2.next
                sum += carry
                cur.next = ListNode(sum % 10)
                cur = cur.next   # 下一个节点
                carry = (sum >= 10)
            if carry:
                cur.next = ListNode(1)
        return ret_Last.next


if __name__ == '__main__':
    res = ListNode(0)
    l1 = res
    l1.next = ListNode(5)
    l1 = l1.next
    l1.next = ListNode(3)
    res2 = ListNode(0)
    l2 = res2
    l2.next = ListNode(5)
    l2 = l2.next
    l2.next = ListNode(3)
    sol = Solution()
    res3 = sol.addTwoNumbers(res.next, res2.next)
    while res3:
        print(res3.val)
        res3 = res3.next
# res = ListNode(0)
# cur = res
# cur.next = ListNode(2)
# cur = cur.next
# cur.next = ListNode(3)
# cur = cur.next
# for i in xrange(10):
#     cur.next = ListNode(i)
#     cur = cur.next
#
# while res:
#     print res.val
#     res = res.next
# s = "pwwkew"
# print len(set(s))
