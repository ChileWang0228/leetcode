#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 23:19
@Author:ChileWang
@algorithm：
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                             4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
                     }
        base_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000][::-1]
        res_str = ''  # 存放结果
        res = num
        for base in base_list:
            base_num = res / base  # 基数对应的个数
            res = res % base
            while base_num:
                res_str += int2roman.get(base)
                base_num -= 1
        return res_str


if __name__ == '__main__':
    sol = Solution()
    print sol.intToRoman(27)





