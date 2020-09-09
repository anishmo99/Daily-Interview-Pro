class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev, copy_x = 0, x
        
        while copy_x != 0:
            r = copy_x%10
            rev = rev*10 + r
            copy_x /= 10
            
        if rev == x:
            return True
        return False