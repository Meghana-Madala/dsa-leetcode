class Solution:
    def addDigits(self, num: int) -> int:
        digits_sum = 0
        while(num > 0):
            digits_sum += num%10
            num //= 10
        if digits_sum > 9:
            return self.addDigits(digits_sum)
        return digits_sum

        