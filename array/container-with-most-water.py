class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_res = 0
        while left < right:
            width = right - left
            #compute the area
            max_res = max(max_res, width*min(height[left], height[right]))
            #updatet the pointer based on the bottle nack
            if height[left] <= height[right]:
                left +=1
            else:
                right-=1
        return max_res