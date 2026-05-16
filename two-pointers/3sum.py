class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue 
            target = -nums[i]
            l, r = i + 1, n-1

            while l < r : 
                s = nums[l] + nums[r]
                if s == target: 
                    res.append([nums[i], nums[l], nums[r]])

                    l_val, r_val = nums[l], nums[r]

                    while l < r and nums[l] == l_val: 
                        l += 1 
                    while l < r and nums[r] == r_val: 
                        r -= 1 

                elif s < target: 
                    l += 1 
                else: 
                    r -= 1 

        return res 