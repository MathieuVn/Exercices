# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Solution(object):

    def largestRectangleArea(self, height):
        """
        :type height: list[int]
        :rtype: int
        """
        max_area = 0

        if len(height) == 0:
            height = [0]
        lenght = len(height)
        half = max(int(round(lenght / 2, 0)), 1)

        if sum(height[:half]) / half < sum(height[half:]) / half:
            height.reverse()
        for i in range(lenght):
            if i > 0 and height[i - 1] >= height[i]:
                continue
            else:
                mini_col = 0
                for j in range(i, lenght):
                    if j == i:
                        mini_col = height[i]
                        max_area = max(max_area, mini_col)
                    elif height[j] < mini_col:
                        max_area = max(max_area, (j - i) * mini_col)
                        mini_col = height[j]
                    elif j == lenght - 1:
                        max_area = max(max_area, (j - i + 1) * mini_col)
                    else:
                        continue
        return max_area

    def largestRectangleArea2(self, height):
        """
        :type height: list[int]
        :rtype: int
        """
        max_area = 0

        if len(height) == 0:
            height = [0]
        lenght = len(height)
        half = max(int(round(lenght / 2, 0)), 1)

        if sum(height[:half]) / half >= sum(height[half:]) / half:
            for i in range(lenght):
                if i > 0 and height[i - 1] >= height[i]:
                    continue
                else:
                    mini_col = 0
                    for j in range(i, lenght):
                        if j == i:
                            mini_col = height[i]
                            max_area = max(max_area, mini_col)
                        elif j == lenght - 1:
                            mini_col = min(mini_col, height[j])
                            max_area = max(max_area, (j - i + 1) * mini_col)
                        elif height[j] >= mini_col:
                            continue
                        else:
                            max_area = max(max_area, (j - i) * mini_col)
                            mini_col = height[j]
        else:
            for i in range(lenght - 1, -1, -1):
                if i < lenght - 1 and height[i + 1] >= height[i]:
                    continue
                else:
                    mini_col = 0
                    for j in range(i, -1, -1):
                        if j == i:
                            mini_col = height[i]
                            max_area = max(max_area, mini_col)
                        elif j == 0:
                            mini_col = min(mini_col, height[j])
                            max_area = max(max_area, (i - j + 1) * mini_col)
                        elif height[j] >= mini_col:
                            continue
                        else:
                            max_area = max(max_area, (i - j) * mini_col)
                            mini_col = height[j]
        return max_area