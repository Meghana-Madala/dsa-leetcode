class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        elif len(nums)==2:
            return nums[i] if(nums[i]<nums[j]) else nums[j]
        if(nums[i] < nums[j]):
            return nums[i]
        while(i<j):
            if(nums[i] < nums[j]):
                return nums[j+1]
            else:
                j-=1
        return nums[j+1]