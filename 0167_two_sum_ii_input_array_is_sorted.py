class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left_number_idx = 0
        right_number_idx = n - 1

        while left_number_idx < right_number_idx:
            sum = numbers[left_number_idx] + numbers[right_number_idx]

            if sum == target:
                return [
                    left_number_idx + 1,
                    right_number_idx + 1,
                ]  # +1 Because it's 1-indexed
            elif (
                sum < target
            ):  # If the sum is larger than target, we have to move the right pointer to the left
                left_number_idx += 1
            else:
                right_number_idx -= 1
        return [0, 0]


def case_one():
    numbers = [2, 7, 11, 15]
    target = 9
    output = [1, 2]
    assert (Solution().twoSum(numbers, target)) == output


def case_two():
    numbers = [2, 3, 4]
    target = 6
    output = [1, 3]
    assert (Solution().twoSum(numbers, target)) == output


def case_three():
    numbers = [-1, 0]
    target = -1
    output = [1, 2]
    assert (Solution().twoSum(numbers, target)) == output


def case_four():
    numbers = [0, 0, 3, 4]
    target = 0
    output = [1, 2]
    assert (Solution().twoSum(numbers, target)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
