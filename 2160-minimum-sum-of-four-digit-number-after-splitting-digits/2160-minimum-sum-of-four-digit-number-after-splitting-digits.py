class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num)) 
        return (int(s[0])*10 + int(s[2])) + (int(s[1])*10 + int(s[3]))