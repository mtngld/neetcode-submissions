class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiply = 1
        count_zeros = 0
        for x in nums:
            print("m", multiply)
            if x != 0:
                multiply *= x
            else:
                count_zeros += 1
        
        output = []
        for idx in range(len(nums)):
            if count_zeros == 0:
                output.append(multiply // nums[idx])
            elif count_zeros == 1:
                if nums[idx] == 0:
                    output.append(multiply)
                else:
                    output.append(0)
            elif count_zeros > 1:
                output.append(0)
        
        return output
        

            

            