from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for str in strs:
            sorted_str = sorted(str)
            sorted_str = "".join(sorted_str)
            dd[sorted_str].append(str)

        return list(dd.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

