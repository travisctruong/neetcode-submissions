class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        returned = []

        for i in range(len(nums)):
            fixed = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            while right > left and right != left:
                if nums[left] + nums[right] == fixed:
                    triplet = []
                    triplet.append(nums[i])
                    triplet.append(nums[left])
                    triplet.append(nums[right])
                    if sorted(triplet) not in returned:
                        returned.append(sorted(triplet))
                    break
                elif nums[left] + nums[right] > fixed:
                    right -= 1
                elif nums[left] + nums[right] < fixed:
                    left += 1
        return returned
