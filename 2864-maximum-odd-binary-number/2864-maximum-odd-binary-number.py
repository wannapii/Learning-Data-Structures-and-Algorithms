class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        r =''
        for c in s:
            if c == '1':
                r = c + r
            else:
                r = r + c
        return r[1:] + '1'