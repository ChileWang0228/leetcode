#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-30 09:49
@Author:ChileWang
@algorithm：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        format_dict = {'{': '}', '(': ')', '[': ']'}
        for sub_s in s:
            if stack == []:
                if sub_s not in format_dict.keys():
                    return False
                stack.append(sub_s)
            else:
                if sub_s in format_dict.keys():
                    stack.append(sub_s)
                else:
                    if sub_s != ' ':
                        if format_dict[stack[-1]] == sub_s:
                            stack.pop()
                        else:
                            return False
        if stack:
            return False
        return True



if __name__ == '__main__':
    sol = Solution()
    print sol.isValid(")}{({))[{{[}")
