class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # total = sum(nums)
        # unique = set()
        # for i in nums:
        #     diff = total - i
        #     if diff in unique:
        #         return True
        #     else:
        #         unique.add(diff)
        # return False
        unique_nums = set(nums)
        if len(nums) == len(unique_nums):
            return False
        return True