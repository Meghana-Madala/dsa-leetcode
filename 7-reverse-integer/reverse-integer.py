class Solution:
    def reverse(self, x: int) -> int:
        rev_Int = 0
        i=0
        flag = False
        if x<0:
            flag = True
            x= 0-x
        while(x>0):
            r = x%10
            rev_Int = (rev_Int * 10) + r
            x//=10
            i+=1
        if -2147483648 <= rev_Int <= 2147483647:
            if flag:
                return 0-rev_Int
            return rev_Int
        else:
            return 0