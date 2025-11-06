class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''
        if str(num)[0] in ('4', '9') and num < 1000:
            numeral_comb_list = [(900, 'CM'), (400, 'CD'), (90, 'XC'), (40, 'XL'), (9, 'IX'), (4, 'IV')]
            for number in numeral_comb_list:
                if number[0] <= num:
                    prefix_value, prefix = number[0], number[1]
                    break
        else:
            numeral_list = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
            for number in numeral_list:
                if number[0] <= num:
                    prefix_value, prefix = number[0], number[1]
                    break
        return prefix + self.intToRoman(num - prefix_value)
