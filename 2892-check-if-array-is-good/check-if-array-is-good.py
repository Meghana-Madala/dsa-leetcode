class Solution:
    def isGood(self, nums: List[int]) -> bool:
        large = max(nums)
        n = len(nums)
        if(nums.count(n-1)==2 and large == n-1) and sum(nums) == ((n*(n-1))//2)+ large and min(nums)==1:
            return True
        else: 
            return False
            