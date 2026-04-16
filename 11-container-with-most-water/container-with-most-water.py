class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        max_height = max(height)
        while(left < right):
            max_area = (right-left)*max_height
            if water > max_area:
                break
            water = max(water, (right-left)*min(height[left], height[right]))
            if(height[left] < height[right]):
                left+=1
            elif (height[left] > height[right]):
                right-=1
            else:
                left+=1
                right-=1
        return water
        