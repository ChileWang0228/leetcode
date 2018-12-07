#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 21:54
@Author:ChileWang
@algorithm：
给定一个 32 位有符号整数，将整数中的数字进行反转。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lim = pow(2, 31)
        if x >= 0:
            invx = int(str(x)[::-1])
            if invx > lim - 1:
                return 0
            return invx
        else:
            invx = -int(str(-x)[::-1])
            if invx < -lim:
                return 0
            return invx


if __name__ == '__main__':
    sol = Solution()
    print sol.reverse(1534236469)
