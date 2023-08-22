from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dd = defaultdict(int)

        for i in s:
            dd[i] += 1

        for i in t:
            dd[i] -= 1

        for value in dd.values():
            if value != 0:
                return False

        return True

s = "rat"
t = "car"
print(Solution().isAnagram(s,t))
