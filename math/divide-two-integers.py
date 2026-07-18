class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend = math.floor(dividend) if dividend > 0 else math.ceil(dividend)
        divisor = math.floor(divisor) if divisor > 0 else math.ceil(divisor)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        ret = 0
        sign = 1
        

        if ((dividend > 0 and abs_dividend < 0) or
            (divisor > 0 and abs_divisor < 0) or
            (dividend < 0 and abs_dividend > 0) or
            (divisor < 0 and abs_divisor > 0)):
            sign = -1
        for _ in range(0, abs_dividend, abs_divisor):
            ret += 1
            if (ret * abs_divisor > abs_dividend):
                ret -= 1

        return ret * sign
        