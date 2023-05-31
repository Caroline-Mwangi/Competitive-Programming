class Solution(object):
    def sortColors(self, nums):
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        idx_w = red + white
        idx_b = red + white + blue

        for i in range(red):
            nums[i] = 0
        for i in range(red, idx_w):
            nums[i] = 1
        for i in range(idx_w, idx_b):
            nums[i] = 2
        return nums