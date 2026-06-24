class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for x in nums:
            result = hash.get(x, None)
            if result != None:
                return True
            else:
                hash[x] = 1
        return False