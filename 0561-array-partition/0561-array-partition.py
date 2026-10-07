class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        nums.sort()
        x = range(0, len(nums), 2)
        for i in x:
            s += nums[i]
        return s