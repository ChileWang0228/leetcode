#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-26 21:54
@Author:ChileWang
@algorithm：
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # 暴力法
        # max_area = 0
        # hei_len = len(height)
        # for i in range(hei_len):
        #     for j in range(i+1,hei_len):
        #         temp_area = (j-i) * min(height[i], height[j])
        #         if temp_area > max_area:
        #             max_area = temp_area
        # return max_area

        # 双指针法
        max_area = 0
        start = 0
        end = len(height) - 1
        while end != start:
            temp_area = (end - start) * min(height[start], height[end])
            if temp_area > max_area:
                max_area = temp_area
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area



if __name__ == '__main__':
    sol = Solution()
    hei = [1,8,6,2,5,4,8,3,7]
    print sol.maxArea(hei)

