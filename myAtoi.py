#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 21:54
@Author:ChileWang
@algorithm：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        lim = pow(2, 31)
        neg_int = '^-\d+'
        pos_int = '^\+?\d+'
        s = s.strip()
        neg = re.findall(neg_int, s)
        pos = re.findall(pos_int, s)
        print pos
        if neg:
            neg = int(neg[0])
            if neg < -lim:
                return -lim
            return neg
        if pos:
            pos = int(pos[0])
            if pos > lim - 1:
                return lim - 1
            return pos
        return 0



if __name__ == '__main__':
    sol = Solution()
    print sol.myAtoi("+1")