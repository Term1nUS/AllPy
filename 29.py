#29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def sign(x: int) -> int:
            sgn = 1
            if x < 0:
                sgn = -1
            return sgn
        if divisor != 0:
            left32 = -2147483648
            right32 = 2147483647
            if dividend >= right32:
                dividend = right32
            if dividend <= left32:
                dividend = left32
            if divisor >= right32:
                divisor = right32
            if divisor <= left32:
                divisor = left32
            dvdnd = abs(dividend)
            dvsr = abs(divisor)
            res = 0
            while dvdnd >= dvsr:
                dvdnd -= dvsr
                res += 1
            print(res)
        return res*sign(dividend)*sign(divisor)


s = Solution()
print(s.divide(100000, 7))