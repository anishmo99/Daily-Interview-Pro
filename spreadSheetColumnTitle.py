class Solution:
    def convertToTitle(self, n):
        res = ''
        while n != 0:
            n -= 1
            temp = chr(ord('A') + (n % 26))
            res = temp + res
            n //= 26
        return res
        

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB