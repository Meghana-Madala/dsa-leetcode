class Solution:
    def outputMethod(self, a: str, b: str, m: int, n: int) -> str:
        output = ""
        carry = '0'
        i = n-1
        j = m-1
        while(i>=0):
            if (a[j] == '1' and b[i] == '1'):
                output+=carry
                carry = '1'
            elif(a[j] == '0' and b[i] == '0'):
                output+=carry
                carry = '0'
            else:
                if carry == '0':
                    output+='1'
                else:
                    output+='0'
                    carry = '1'
            i-=1
            j-=1
        while(j>=0 and carry == '1'):
            if a[j] == '1':
                output+='0'
                carry = '1'
            else:
                output += '1'
                carry = '0'
            j-=1
        if carry == '1':
            output+='1'
        if j>=0:
            return a[:j+1]+output[::-1]
        return output[::-1]
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        if m >= n:
            return self.outputMethod(a,b, m, n)
        return self.outputMethod(b,a, n, m)
            

                    
        