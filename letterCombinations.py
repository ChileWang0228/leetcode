#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-28 23:01
@Author:ChileWang
@algorithm：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
解法：利用字典
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) < 1:
            return []
        digit2letter = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        letter_list = []
        for digit in digits:
            letter_list.append(digit2letter[digit])
        result = dict()
        for letter in letter_list[0]:
            result[letter] = letter
        for i in range(1, len(letter_list)):
            for key in result.keys():
                result.pop(key)  # 删除对应的键
                for letter in letter_list[i]:
                        k1 = key + letter
                        result[k1] = k1

        return result.values()


if __name__ == '__main__':
    sol = Solution()

    print sol.letterCombinations("")