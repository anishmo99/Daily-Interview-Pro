class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  return 0
        
        prod, ans, left = 1, 0, 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            
            while prod >= k:    
                prod /= nums[left]
                left += 1
                
            ans += right - left + 1
            
        return ans