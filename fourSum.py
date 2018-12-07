#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-28 23:01
@Author:ChileWang
@algorithm：给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #  双指针法
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        res = dict()
        for i in range(len(nums)):
            fix1 = nums[i]
            for j in range(i + 1, len(nums)):
                fix2 = nums[j]
                start = j + 1
                end = len(nums) - 1

                while start < len(nums) and start < end:
                    flag = nums[end] + nums[start] + fix1 + fix2
                    if flag > target:
                        end -= 1
                    if flag < target:
                        start += 1
                    if flag == target:
                        res[(fix1, fix2, nums[start], nums[end])] = 1
                        start += 1
                        end -= 1
        result = []
        for item in res.keys():
            result.append(list(item))
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.fourSum([1,0,-1,0,-2,2], 1)
