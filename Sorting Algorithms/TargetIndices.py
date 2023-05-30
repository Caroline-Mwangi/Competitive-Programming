class Solution(object):
    def targetIndices(self, nums, target):
        srt = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if srt[i] == target:
                res.append(i)
        return res