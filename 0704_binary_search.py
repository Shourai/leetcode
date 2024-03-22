class Solution:
    def search(self, nums: list[int], target: int) -> int:
        output = -1
        n = len(nums)
        L = 0
        R = n - 1

        while L <= R:
            m = (L + R) // 2
            print(m)
            if nums[m] < target:
                L = m + 1
            elif nums[m] > target:
                R = m - 1
            elif nums[m] == target:
                return m
        return output


def case_one():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    output = 4
    print(Solution().search(nums, target))
    assert (Solution().search(nums, target)) == output


def case_two():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    output = -1
    print(Solution().search(nums, target))
    assert (Solution().search(nums, target)) == output


def case_three():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 9
    output = 8
    print(Solution().search(nums, target))
    assert (Solution().search(nums, target)) == output


def case_four():
    nums = [5]
    target = 5
    output = 0
    print(Solution().search(nums, target))
    assert (Solution().search(nums, target)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
