#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 14:05
@Author:ChileWang
@algorithm：马拉车算法
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        #  每个字符插入#, 特殊字符为@
        ss = '@' + '#'.join([x for x in s]) + '$'
        print ss
        p = [0] * len(ss)  # 半径矩阵
        center = 0
        mx = 0
        max_str = ''
        for i in range(1, len(ss)-1):
            if i < mx:
                j = 2 * center - i  # j是i关于center的对称点
                p[i] = min(mx - i, p[j])

            # 尝试向两边拓展

            while ss[i - p[i] - 1] == ss[i + p[i] + 1]:
                p[i] += 1

                # 不必判断溢出，两端均是特殊字符，会自动检测并退出

            # 更新中心
            if i + p[i] > mx:
                mx = i + p[i]
                center = i
            # 更新最长串
            if 1 + 2 * p[i] >= len(max_str):
                temp = ss[i-p[i]:i+p[i]+1]
                if len(temp.replace('#', '')) > len(max_str.replace('#', '')):
                    max_str = temp

        return max_str.replace('#', '')






        # 暴力法
        # print invs
        # max_len = 0
        # fina_start = 0
        # fina_end = 0
        # for i in xrange(len(s)):
        #
        #     start_index = i
        #     j = len(s) - 1
        #     end_index = j
        #     while_len = j - i + 1  # 本次循环长度
        #     if max_len > while_len:
        #         print max_len, while_len
        #         break
        #     while j > i:
        #         if max_len > while_len:  # 大于本次循环长度则说明，本次循环找到的子串长度都小于max_len
        #             #print max_len, while_len
        #             break
        #         if s[i] == s[j]:
        #             j -= 1
        #             i += 1
        #             if i == j or j < i:  # 找到最大值
        #                 if end_index - start_index + 1 >= max_len:
        #                     max_len = end_index - start_index + 1
        #                     fina_end = end_index
        #                     fina_start = start_index
        #                     while_len = end_index - start_index   # 下次循环长度
        #         else:
        #             j = end_index - 1
        #             i = start_index
        #             end_index = j
        #             while_len = j - i + 1  # 本次循环长度
        #
        #abacdfg
        # print fina_start, fina_end
        # return s[fina_start:fina_end + 1]



if __name__ == '__main__':
    sol = Solution()
    #print sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #print sol.longestPalindrome("aaaabaaa")
    #print sol.longestPalindrome('abacdfgdcaba')
    print sol.longestPalindrome('abb')