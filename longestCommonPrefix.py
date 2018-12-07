#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-27 00:16
@Author:ChileWang
@algorithm：编写一个函数来查找字符串数组中的最长公共前缀。

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        comfre = ''
        if len(strs) == 0:
            return comfre

        min_str_len = len(strs[0])  # 找出三个字符串中最短的那个
        for s in strs:
            if min_str_len > len(s):
                min_str_len = len(s)
        flag = 1  # 前缀相同标记
        for i in range(min_str_len):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if temp != strs[j][i]:
                    flag = 0
                    break
            if flag:
                comfre += temp
            else:
                break
        return comfre


if __name__ == '__main__':
    sol = Solution()
    print sol.longestCommonPrefix( ["dog","racecar","car"])
