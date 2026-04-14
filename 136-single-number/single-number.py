class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single ^= i
        return single
        # single = nums[0]
        # for i in range(1, len(nums)):
        #     single ^= nums[i]
        # return single