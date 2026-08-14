class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        permitted_letters = "abcdef"
        if "." in queryIP:
            list_nums = queryIP.split(".")
            if len(list_nums) != 4:
                return "Neither"
            for num in list_nums:
                if not (len(num) > 0 and num.isdigit() and (num[0] != "0" or num == "0") and int(num) < 256):
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            list_nums = queryIP.split(":")
            if len(list_nums) != 8:
                return "Neither"
            for num in list_nums:
                if not (len(num) >= 1 and len(num) <= 4):
                    return "Neither"
                for char in num:
                    if not char.isdigit() and not (char.isalpha() and char.lower() in permitted_letters):
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"