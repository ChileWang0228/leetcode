#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-24 14:05
@Author:ChileWang
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = dict()
        max_len = 0
        for i in xrange(len(s)):
            if s[i] not in substr.keys():
                substr[s[i]] = i
                print(substr)
            else:
                if len(substr) > max_len:
                    max_len = len(substr)
                begin_index = substr[s[i]] + 1  # 从不重复的那个字符开始添加到字典里，这样保证了序号连贯性
                substr.clear()
                for j in xrange(begin_index, i+1):
                    substr[s[j]] = j

        if max_len < len(substr):
            max_len = len(substr)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstring("dvdf")
    print sol.lengthOfLongestSubstring("pwwkew")
    print sol.lengthOfLongestSubstring("")
    print sol.lengthOfLongestSubstring(" ")