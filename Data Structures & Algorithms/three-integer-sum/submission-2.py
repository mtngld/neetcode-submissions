class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ptr_target = 0
        result = []

        while ptr_target < len(nums) - 2:
            if ptr_target > 0 and nums[ptr_target] == nums[ptr_target - 1]:
                ptr_target += 1
                continue
            
            curr_target = -nums[ptr_target]
            ptr_left = ptr_target + 1
            ptr_right = len(nums) - 1
            while ptr_left < ptr_right:
                if nums[ptr_left] + nums[ptr_right] == curr_target:
                    result.append([nums[ptr_target], nums[ptr_left], nums[ptr_right]])
                    ptr_left += 1
                    ptr_right -= 1
                    while ptr_left < ptr_right and nums[ptr_left] == nums[ptr_left - 1]:
                        ptr_left += 1
                    while ptr_left < ptr_right and nums[ptr_right] == nums[ptr_right + 1]:
                        ptr_right -= 1
                elif nums[ptr_left] + nums[ptr_right] < curr_target:
                    ptr_left += 1
                elif nums[ptr_left] + nums[ptr_right] > curr_target:
                    ptr_right -= 1
            ptr_target += 1
        return result
