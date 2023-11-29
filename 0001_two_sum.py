class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class Solution2:
    """
    Use a dictionary to save the complement as key and the index as value
    e.g. case one
    After the first run the complement dict will be of {target - cur num:  idx} => {9 - 2: 0} => {7: 0}
    On the second run, it will find the complement in the dictionary,
    so it returns the index of the complement in the dictionary (i.e. 0 in this case)
    and the index of the current number i.e. 1 (which is the complement).
    So it returns [0, 1]
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement = {}
        for idx, n in enumerate(nums):
            if n in complement:
                return [complement[n], idx]
            else:
                complement[target - n] = idx
        return []


def case_one():
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target)) == [0, 1]
    assert (Solution2().twoSum(nums, target)) == [0, 1]


def case_two():
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target)) == [1, 2]
    assert (Solution2().twoSum(nums, target)) == [1, 2]


def case_three():
    nums = [3, 3]
    target = 6
    assert (Solution().twoSum(nums, target)) == [0, 1]
    assert (Solution2().twoSum(nums, target)) == [0, 1]


def case_four():
    nums = [2, 5, 5, 11]
    target = 10
    assert (Solution().twoSum(nums, target)) == [1, 2]
    assert (Solution2().twoSum(nums, target)) == [1, 2]


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
