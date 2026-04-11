class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # res = []
        # num = 0
        # for i in range(len(digits)):
        #     num = digits[len(digits) - i - 1] * (10**i) + num
        # num+=1
        # while(num > 0):
        #     res.insert(0,num % 10)
        #     num = num // 10
        # return res

        for i in range(len(digits)-1, -1, -1):
            if(digits[i] < 9):
                digits[i]+=1
                return digits
            digits[i] = 0
        digits = [0]*(len(digits)+1)
        digits[0] = 1
        return digits
        

        