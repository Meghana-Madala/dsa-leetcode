class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        rev_Int = 0
        while(x>0):
            rev_Int = (rev_Int*10) + (x%10)
            x//=10
            if not(-2147483648 <= rev_Int <= 2147483647):
                return 0
        return rev_Int*sign 
