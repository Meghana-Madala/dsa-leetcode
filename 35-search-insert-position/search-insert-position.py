class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (len(nums) == 0):
            return 
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        if ((nums[left] == target) or (nums[left] > target)):
            return left
        else: 
            return left+1