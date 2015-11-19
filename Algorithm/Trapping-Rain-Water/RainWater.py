# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:48:38 2015

@author: a998473
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Init
        n = len(height)

        leftHighest = [0] * n
        rightHighest = [0] * n
        leftHighSoFar = 0
        rightHighSoFar = 0

        waterVol = 0

        # Get the rolling highest height from left side
        for i in range(n):
            leftHighest[i] = leftHighSoFar
            leftHighSoFar = max(leftHighSoFar, height[i])

        # Get the rolling highest height from right side
        for i in range(n - 1, -1, -1):
            rightHighest[i] = rightHighSoFar
            rightHighSoFar = max(rightHighSoFar, height[i])

        # Compute the volume of water
        for i in range(n):
            waterVol += max(0, min(leftHighest[i], rightHighest[i]) - height[i])

        return waterVol
