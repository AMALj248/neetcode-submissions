class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        
        max_area = 0
        while(i<j):
            w = j-i
            h = min(height[i], height[j])
            curr_area = w*h
            max_area = max(curr_area, max_area)
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            elif height[i] == height[j]:
                i+=1
                j-=1
        return max_area