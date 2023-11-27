class Solution:
    "Using a dictionary as counter"

    def containsDuplicate(self, nums: list[int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        for val in counter.values():
            if val > 1:
                return True

        return False


class Solution2:
    "Using a set"

    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False


def case_one():
    nums = [1, 2, 3, 1]
    assert (Solution().containsDuplicate(nums)) is True
    assert (Solution2().containsDuplicate(nums)) is True


def case_two():
    nums = [1, 2, 3, 4]
    assert (Solution().containsDuplicate(nums)) is False
    assert (Solution2().containsDuplicate(nums)) is False


def case_three():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert (Solution().containsDuplicate(nums)) is True
    assert (Solution2().containsDuplicate(nums)) is True


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
