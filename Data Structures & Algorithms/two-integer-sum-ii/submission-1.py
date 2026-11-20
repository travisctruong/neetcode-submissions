class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        returned = []

        while left != right:
            total = numbers[left] + numbers[right]
            if total == target:
                returned.append(numbers[left])
                returned.append(numbers[right])
                return returned
            
            elif total > target:
                right -= 1
            elif total < target:
                left += 1
        return returned
