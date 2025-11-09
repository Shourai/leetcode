class Solution(object):
    def findMissingElements(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        lowest = nums[0]
        highest = nums[-1]

        lst = []
        for i in range(lowest, highest):
            if i not in nums:
                lst.append(i)
        return lst


def case_one():
    nums = [1, 4, 2, 5]
    print(Solution().findMissingElements(nums))


def case_two():
    nums = [6, 7, 8, 9]
    print(Solution().findMissingElements(nums))


def case_three():
    nums = [5, 1]
    print(Solution().findMissingElements(nums))


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
