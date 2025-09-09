class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        for i in range(len(nums)):
            if nums[p2] == val and p2 >= i:
                p2 -= 1
            if nums[i] == val and p2 >= i:
                tmp = nums[i]
                nums[i] = nums[p2]
                nums[p2] = tmp
                p2 -= 1
        nums[:] = nums[0:nums.index(val)]


def case_one():
    nums = [3, 2, 2, 3]
    val = 3
    Solution().removeElement(nums,val)


def case_two():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    Solution().removeElement(nums,val)


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
