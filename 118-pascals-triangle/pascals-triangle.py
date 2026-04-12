class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            row = []
            value = 1
            row.append(value)
            for k in  range(1,i):
                value = value * (i - k) // k
                row.append(value)
            res.append(row)
        return res