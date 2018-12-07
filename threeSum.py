#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-27 00:16
@Author:ChileWang
@algorithm：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 暴力法
        # nums = sorted(nums)
        # nums_set = dict()
        # num_len = len(nums)
        # for i in range(num_len):
        #     for j in range(i+1, num_len):
        #         for k in range(j+1, num_len):
        #             if nums_set.has_key((nums[i], nums[j], nums[k])):
        #                 pass
        #             else:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     nums_set[(nums[i], nums[j], nums[k])] = 1
        # return nums_set.keys()


        #  双指针法
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] > 0:  # 若第一个数大于0，接下来相加不可能等于0
                break
            fix = nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < len(nums) and start < end:
                flag = nums[end] + nums[start] + fix
                if flag > 0:
                    end -= 1
                if flag < 0:
                    start += 1
                if flag == 0:
                    nums_dict[(fix, nums[start], nums[end])] = 1
                    start += 1
                    end -= 1

        return nums_dict.keys()


if __name__ == '__main__':
    sol = Solution()
    print sol.threeSum([-2,0,1,1,2])
