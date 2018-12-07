#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-30 16:00
@Author:ChileWang
@algorithm：
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6



"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = []
        for l in lists:
            cur = l
            while cur:
                result_list.append(cur.val)
                cur = cur.next

        result_list.sort()

        head = ListNode(-1)
        cur = head
        for num in result_list:
            cur.next = ListNode(num)
            cur = cur.next
        return head.next


if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l = []
    l.append(l1)
    l.append(l2)
    cur = sol.mergeKLists(l)
    while cur:
        print cur.val
        cur = cur.next