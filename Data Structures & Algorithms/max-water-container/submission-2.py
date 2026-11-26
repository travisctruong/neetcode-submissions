class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            output = max(output, height * width)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                
        return output



                