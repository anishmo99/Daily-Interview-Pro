class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxr, maxl = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        
        maxl[0] = height[0]
        for i in range(1, len(height)):
            maxl[i] = max(maxl[i - 1], height[i])
            
        maxr[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            maxr[i] = max(maxr[i + 1], height[i])
            
        water = [min(maxl[i], maxr[i]) - height[i] for i in range(len(height))]
        
        return sum(water)