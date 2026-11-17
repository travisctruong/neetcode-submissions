class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = dict()

        for i in nums:
            if dupes.get(i) is None:
                dupes[i] = 1
            else:
                return True
                
        return False
