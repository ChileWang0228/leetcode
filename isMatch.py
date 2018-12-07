#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 21:54
@Author:ChileWang
@algorithm：
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
"""
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s1 = re.findall(p, s)
        # print s1[0]
        if s1:
            if s1[0] == s:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s = "ab"
    p = ".*c"
    print sol.isMatch(s,p)