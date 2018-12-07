#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-28 23:01
@Author:ChileWang
@algorithm：给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closet_sum = 999999999
        nums = sorted(nums)
        result = 0
        for i in range(len(nums)):
            fix = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < len(nums) and start < end:
                flag = nums[end] + nums[start] + fix
                dist = abs(flag - target)

                if closet_sum > dist:
                    closet_sum = dist
                    result = flag

                if flag > target:
                    end -= 1
                if flag < target:
                    start += 1
                if flag == target:
                    break


        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumClosest([0,2,1,-3], 0)