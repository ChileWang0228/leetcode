#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-10-24 14:05
@Author:ChileWang
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        while len1 or len2:
            if len1 == 0:
                if len2 % 2 == 0:
                    return (nums2[len2 / 2] + nums2[(len2 / 2) - 1]) / 2.0
                else:
                    return nums2[(len2+1) / 2 - 1]
            if len2 == 0:
                if len1 % 2 == 0:
                    return (nums1[len1 / 2] + nums1[(len1 / 2) - 1]) / 2.0
                else:
                    return nums1[(len1+1) / 2 - 1]

            len_all = len1 + len2
            res_num = nums2 + nums1
            res_num = sorted(res_num)
            print res_num
            if len_all % 2 == 0:
                res_index1 = len_all / 2
                res_index2 = res_index1 - 1
                return (res_num[res_index1] + res_num[res_index2]) / 2.0
            else:
                res_index = (len_all + 1) / 2 - 1
                return res_num[res_index]


if __name__ == '__main__':
    nums1 = [2,3]
    nums2 = []
    sol = Solution()
    print sol.findMedianSortedArrays(nums1, nums2)


