class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        num = 0
        for i in range(len(digits)):
            num = digits[len(digits) - i - 1] * (10**i) + num
        num+=1
        while(num > 0):
            res.insert(0,num % 10)
            num = num // 10
        return res

        