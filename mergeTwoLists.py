#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-30 16:00
@Author:ChileWang
@algorithm：
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = []
        cur = l1
        while cur:
            result_list.append(cur.val)
            cur = cur.next
        cur = l2
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
    cur = sol.mergeTwoLists(l1, l2)
    while cur:
        print cur.val
        cur = cur.next
