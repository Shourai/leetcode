from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False




nums = [1,1,1,3,3,4,3,2,4,2]

print(Solution().containsDuplicate(nums))
