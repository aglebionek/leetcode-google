from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height) - 1
        area = 0
        left = 0
        right = length
        left_height = height[left]
        right_height = height[right]
        while length > 0:
            area = max(area, length * min(left_height, right_height))
            length -= 1
            if left_height < right_height:
                left += 1
                left_height = height[left]
                continue
            right -= 1
            right_height = height[right]
            
        return area
    