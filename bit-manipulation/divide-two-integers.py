class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # Handle overflow case explicitly
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive values
        dvd = abs(dividend)
        dvs = abs(divisor)

        result = 0

        # Main loop: subtract largest shifted divisor each time
        while dvd >= dvs:
            shift = 0
            # Find largest shift such that (dvs << shift) <= dvd
            while dvd >= (dvs << (shift + 1)):
                shift += 1

            dvd -= dvs << shift
            result += 1 << shift

        if negative:
            result = -result

        # Clamp to 32-bit range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result