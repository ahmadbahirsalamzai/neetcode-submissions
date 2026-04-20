class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        # move right to the left as long as the hieght to the left is smaller than left.  

        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]

            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
            # else:
            #     r -= 1
            #     maxR = max(maxR, height[r])
            #     res += maxR - height[r]
                
        return res
                



            