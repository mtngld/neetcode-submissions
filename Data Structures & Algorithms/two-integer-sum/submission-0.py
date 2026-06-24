class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, x in enumerate(nums):
            if target - x in d:
                return [d[target - x], idx]
            else:
                d[x] = idx
