class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1

        sorted_values = sorted(hashmap, key=hashmap.get, reverse=True)  

        return sorted_values[:k]          

