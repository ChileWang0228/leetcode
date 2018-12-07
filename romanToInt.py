#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 23:19
@Author:ChileWang
@algorithm：
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
                     }
        base_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = 0
        i = 0
        for base in base_list:
            if i >= len(s):
                break
            base_len = len(base)

            if base_len == 1:
                while i < len(s) and s[i] == base:
                    res += roman2int.get(base)
                    i += 1
            else:
                while i+1 < len(s) and s[i]+s[i+1] == base:
                        res += roman2int.get(base)
                        i += 2
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.romanToInt("DCXXI")


