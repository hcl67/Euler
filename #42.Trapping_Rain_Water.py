'''
https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        if n <= 1:
            return 0
        damq = [0]
        wlvl = height[0]
        for i in range(1,n):
            if height[i] < height[damq[-1]]:
                damq += [i]
                wlvl = height[i]
            elif height[i] == height[damq[-1]]:
                damq[-1] = i
            elif height[i] > height[damq[-1]]:
                while len(damq) > 0:
                    if height[damq[-1]] <= height[i]:
                        ans += (min(height[i],height[damq[-1]])-wlvl)*(i-damq[-1]-1)
                        wlvl = min(height[i],height[damq[-1]])
                        del damq[-1]
                    else:
                        ans += (min(height[i],height[damq[-1]])-wlvl)*(i-damq[-1]-1)
                        wlvl = min(height[i],height[damq[-1]])
                        break
                damq += [i]
                wlvl = height[i]
        return ans
                        
                        
                
            
