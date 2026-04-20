class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i=0
        j=len(colors)-1
        if(colors[i]!=colors[j]):
            return j
        max_dist = 1
        while(i<j):
            if(colors[i]==colors[j]):
                j-=1
            else:
                max_dist = j-i
                break

        i=0
        j=len(colors)-1
        while(i<j):
            if(colors[i]==colors[j]):
                i+=1
            else:
                return max(max_dist, j-i)
        