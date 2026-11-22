class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        hashmap = {0: 1}

        for i in nums:
            total += i
            diff = total - k
            if diff in hashmap:
                count += hashmap[diff]
            hashmap[total] = hashmap.get(total, 0) + 1
        return count