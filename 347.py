from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1

        sortedlist = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        l = []
        for i in range(k):
            l.append(sortedlist[i][0])
        heap = []
        return l


nums = [3,0,1,0]
k = 1

print(Solution().topKFrequent(nums, k))

