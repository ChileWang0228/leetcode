#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 16:25
@Author:ChileWang
@algorithm：
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len = len(s)
        if numRows < 2:
            return s

        col_num = s_len
        s_max = [['' for j in range(col_num)] for i in range(numRows)]

        i = 0
        j = 0
        index = 0
        while index != s_len:
            if i < numRows:
                s_max[i][j] = s[index]
                i += 1
                index += 1
            else:
                i -= 2
                while i > 0:
                    j += 1
                    s_max[i][j] = s[index]
                    i -= 1
                    index += 1
                    if index == s_len:
                        break
                j += 1

        ret_str = ''
        for l1 in s_max:
            for l2 in l1:
                if l2:
                    ret_str += l2
        return ret_str


if __name__ == '__main__':
    sol = Solution()
    #print sol.convert("ABCDE", 4)
    # print sol.convert("ABC", 1)
    #print sol.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 4)
