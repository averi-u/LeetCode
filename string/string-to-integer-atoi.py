class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        while i < n and s[i] == '': 
            i += 1 

        sign = 1 
        if i < n and (s[i] == '+' or s[i] == '-'): 
            if s[i] == '-': 
                sign = -1 
            i += 1 

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 

        num = 0 
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if num > INT_MAX // 10 or (
                num == INT_MAX // 10 and digit > INT_MAX % 10 
            ); 

            