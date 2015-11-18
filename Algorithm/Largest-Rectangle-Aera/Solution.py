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
        # Init max_area variable
        max_area = 0

        # Case when height in empty
        if len(height) == 0:
            height = [0]
        # Get the variable length and the integer half of length
        length = len(height)
        half = max(int(round(length / 2, 0)), 1)

        # Flip the variable height to get the highest values near of the index 0 (left side)
        if sum(height[:half]) / half < sum(height[half:]) / half:
            height.reverse()
        # For each columns (i.e. items of the list height)
        for i in range(length):
            if i > 0 and height[i - 1] >= height[i]:
                continue
            else:
                mini_col = 0
                for j in range(i, length):
                    if j == i:
                        mini_col = height[i]
                        max_area = max(max_area, mini_col)
                    elif height[j] < mini_col:
                        max_area = max(max_area, (j - i) * mini_col)
                        mini_col = height[j]
                    elif j == length - 1:
                        max_area = max(max_area, (j - i + 1) * mini_col)
                    else:
                        continue
        return max_area
