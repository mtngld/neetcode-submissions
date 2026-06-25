class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr_left = 0
        ptr_right = len(s) - 1
        while ptr_left < ptr_right:
            print(s[ptr_left])
            print(s[ptr_right])
            if not s[ptr_left].isalnum():
                ptr_left += 1
            
            elif not s[ptr_right].isalnum():
                ptr_right -= 1

            elif s[ptr_left].lower() == s[ptr_right].lower():
                ptr_left += 1
                ptr_right -= 1
            else:
                return False
        return True