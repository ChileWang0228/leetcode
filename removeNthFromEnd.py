#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-30 09:49
@Author:ChileWang
@algorithm：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_list_len(self, head):
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next
        return list_len

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        list_len = self.get_list_len(head)
        delete_index = list_len - n + 1  # 被删除节点的索引
        if delete_index == 1:  # 索引为第一个
            return head.next
        else:
            pre = head
            cur = head.next
            index = 2
            while cur:
                if index == delete_index:
                    break
                index += 1
                pre = cur
                cur = cur.next
            pre.next = cur.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    cur.next = ListNode(2)
    cur.next.next = ListNode(3)
    cur.next.next.next = ListNode(4)
    cur.next.next.next.next = ListNode(5)
    sol = Solution()
    cur = sol.removeNthFromEnd(head, 2)
    while cur:
        print cur.val
        cur = cur.next

