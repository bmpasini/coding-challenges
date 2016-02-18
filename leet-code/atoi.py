# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not
# see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        num = 0
        sign = None
        if str[0] == "+" or str[0] == "-":
            sign = str[0]
            str = str[1:]
        for i, char in enumerate(str):
            try:
                num += (10 ** (len(str)-i-1)) * int(char)
            except ValueError:
                num /= (10 ** (len(str)-i))
                break
        if sign is not None and sign == "-":
            if num > 2147483648:
                num = 2147483648
            return -num
        if num > 2147483647:
            num = 2147483647
        return num