class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        # max_dist = 0
        # for j in range(len(nums2)-1, -1, -1):
        #     l=0
        #     r=len(nums1)-1
        #     while(l <= r):
        #         mid = l + (r-l)//2
        #         if(nums1[mid] <= nums2[j]):
        #             max_dist = max(max_dist, j-mid)
        #             r = mid-1
        #         else:
        #             l = mid+1
                
        #         #mid = (l+r)//2
                
        # return max_dist
        i=0
        j=0
        while(j<len(nums2)):
            if(nums1[i] > nums2[j]):
                i+=1
            j+=1
            if i >= len(nums1):
                    break
        return max(j-i-1,0)
                