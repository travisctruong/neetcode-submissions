class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            returned = []
            complement = target - nums[i]
            if complement in hashmap:
                returned.append(hashmap[complement])
                returned.append(i)
                return returned
            else:
                if nums[i] not in hashmap:
                    hashmap[nums[i]] = i
            
