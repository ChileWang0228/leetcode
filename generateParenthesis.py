#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-30 16:10
@Author:ChileWang
@algorithm： 回溯法
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def backtrack(self, ans, s, left, right, n):
        if len(s) == 2 * n:
            ans.append(s)
        if left < n:
            self.backtrack(ans, s+'(', left + 1, right, n)
        if right < left:
            self.backtrack(ans, s+')', left, right + 1, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ans = []
        left = 0
        right = 0
        s = ''
        self.backtrack(ans, s, left, right, n)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print sol.generateParenthesis(3)