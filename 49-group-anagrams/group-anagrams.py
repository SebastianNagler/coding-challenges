from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_sorted_strings = {}
        output = []

        for s in strs:
            s_sorted = str(sorted(s))
            if s_sorted in dict_of_sorted_strings:
                output[dict_of_sorted_strings[s_sorted]].append(s)
            else:
                dict_of_sorted_strings[s_sorted] = len(output)
                output.append([s])
        
        return output



        