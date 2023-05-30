class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)

        srt = sorted(nums)

        res = [None] * n

        for i in range(n):
            res[i] = srt.index(nums[i])
        return res