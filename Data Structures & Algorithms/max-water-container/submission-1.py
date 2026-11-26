class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        left = 0
        right = len(heights) - 1
        while left < right and left != right:
            width = right - left
            left_val = heights[left]
            right_val = heights[right]
            height = min(left_val, right_val)

            if width * height > output:
                output = width * height

            if left_val > right_val:
                right -= 1
            elif left_val < right_val:
                left += 1
            else:
                left += 1
                right -= 1
                
        return output



                