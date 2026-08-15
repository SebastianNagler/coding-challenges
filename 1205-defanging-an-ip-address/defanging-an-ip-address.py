class Solution:
    def defangIPaddr(self, address: str) -> str:
        num_list = address.split(".")
        return "[.]".join(num_list)