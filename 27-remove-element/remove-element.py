class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return
        endIndex = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if (nums[i] == val):
                nums[i] = nums[endIndex]
                endIndex-=1
        return endIndex+1
