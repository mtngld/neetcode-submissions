class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        curr_consecutive = 0
        for x in nums:
            if x == 1:
                curr_consecutive += 1
            else:
                if curr_consecutive > curr_max:
                    curr_max = curr_consecutive
                curr_consecutive = 0
        
        if curr_consecutive > curr_max:
            curr_max = curr_consecutive
            
        return curr_max


