class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)   
        # Storing a value also increase runtime I guess its because need to   retrieve and verify it matches or not
        i = 0
        j = i+1
        # while(i<n and j < n):
        #     while(j < n and nums[i] == nums[j]):
        #         j+=1
        #     if j < n:
        #         nums[i+1] = nums[j]
        #         i+=1
        #         j+=1
        # return i+1
        if len(nums) == 0:
            return 0
        while (i <= j and j < len(nums)):
            if (nums[i] == nums[j]):
                j+=1
            else:
                nums[i+1] = nums[j]
                i+=1
                # j+=1
        return i+1