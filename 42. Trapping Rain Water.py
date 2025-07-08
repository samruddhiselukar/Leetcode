# 2 pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0
        while l < r: #[0,1,0,2,1,0,1,3,2,1,2,1]
            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
            else:
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]

        return water
