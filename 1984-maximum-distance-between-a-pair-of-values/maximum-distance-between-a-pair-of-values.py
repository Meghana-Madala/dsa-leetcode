class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[len(nums1)-1] > nums2[0]:
            return 0
        max_dist = 0
        for j in range(len(nums2)-1, -1, -1):
            l=0
            r=len(nums1)-1
            while(l <= r):
                mid = l + (r-l)//2
                if(nums1[mid] <= nums2[j]):
                    # if((mid-1 < 0) or (nums1[mid-1] > nums2[j])):
                    #     return j-mid
                    max_dist = max(max_dist, j-mid)
                    r = mid-1
                else:
                    l = mid+1
                
                #mid = (l+r)//2
                
        return max_dist
                