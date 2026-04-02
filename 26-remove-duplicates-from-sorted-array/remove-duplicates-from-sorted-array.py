class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = i+1
        while(i<n and j < n):
            while(j < n and nums[i] == nums[j]):
                j+=1
            if j < n:
                nums[i+1] = nums[j]
                i+=1
                j+=1
        return i+1