class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')
        zipped = itertools.zip_longest(list1, list2, fillvalue='0')
        for s1, s2 in zipped:
            if int(s1) < int(s2):
                return -1
            if int(s1) > int(s2):
                return 1
        return 0