class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_left = 0
        ptr_right = len(numbers) - 1

        while True:
            if ptr_left == ptr_right:
                raise Exception("no solution!")
            current_sum = numbers[ptr_left] + numbers[ptr_right]
            if current_sum == target:
                return [ptr_left + 1, ptr_right + 1]
            elif current_sum < target:
                ptr_left += 1
            else:
                ptr_right -= 1
            
            

