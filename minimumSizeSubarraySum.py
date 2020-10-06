class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, sum, count = 0, 0, float('inf')
        
        for right in range(len(nums)):
            sum += nums[right]
            
            while sum >= s:
                count = min(count, right - left + 1)
                sum -= nums[left]
                left += 1
                
        return count if count != float('inf') else 0