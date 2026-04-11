class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long= max(strs)
        short=min(strs)
        n=len(short)
        prefix=""
        for i in range(n):
            if(short[i]==long[i]):
                prefix+=short[i]
            else:
                return prefix
        return prefix