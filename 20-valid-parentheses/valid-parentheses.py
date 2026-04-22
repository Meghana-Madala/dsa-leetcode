class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n=len(s)
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif not stack:
                return False
            else:
                curr=s[i]
                curr=stack.pop()+curr
                if not(curr =="()" or curr=="[]" or curr == "{}"):
                    return False
        if not stack:
            return True
        else:
            return False



        