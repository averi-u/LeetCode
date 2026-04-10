class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
                # edge case
        if len(nums) == 0:
            return [-1, -1]
        start_pos = -1
        end_pos = -1

        # first round binary search
        left_start = 0
        right_start = len(nums) - 1
        mid_start = (left_start+right_start) // 2
        print("first part", left_start, right_start)
        while right_start > left_start:
            print(mid_start, nums[mid_start])
            if nums[mid_start] >= target:
                right_start = mid_start
            else:
                left_start = mid_start + 1
            mid_start = (left_start+right_start) // 2
        if nums[mid_start] == target:
            start_pos = mid_start
        left_end = 0
        right_end = len(nums) - 1
        mid_end = (left_end+right_end) // 2
        print("second part", left_end, right_end)
        while left_end < right_end:
            print(mid_end, nums[mid_end], left_end, right_end)
            if nums[mid_end] <= target:
                if (mid_end+1 < len(nums)) and (nums[mid_end+1] > target):
                    break
                left_end = mid_end + 1
            else:
                right_end = mid_end - 1
            mid_end = (left_end+right_end) // 2
        print(mid_end, nums[mid_end], left_end, right_end)    
        if nums[mid_end] == target:
            end_pos = mid_end
        return [start_pos, end_pos]





        # def bound(is_left: bool) -> int: 
            # l, r = 0, len(nums) - 1 
            # ans = -1 
            # while l <= r: 
            #     mid = (l + r) // 2 
            #     if nums[mid] == target: 
            #         ans = mid 
            #         if is_left: 
            
                    