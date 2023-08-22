from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n 
        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] = left
            left = left * nums[i]

        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * right
            right = right * nums[i]

        return ans




nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
