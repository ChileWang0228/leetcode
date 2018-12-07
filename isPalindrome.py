#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 21:54
@Author:ChileWang
@algorithm：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            invx = int(str(x)[::-1])
            if invx == x:
                return  True

        return False



if __name__ == '__main__':
    sol = Solution()
    print sol.isPalindrome(10)