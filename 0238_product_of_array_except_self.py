class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1
        n = len(nums)
        left_array = [0] * n
        right_array = [0] * n

        for i in range(n):
            left_array[i] = left_product
            left_product *= nums[i]

        for i in range(n - 1, -1, -1):
            right_array[i] = right_product
            right_product *= nums[i]

        return [i * j for i, j in zip(left_array, right_array)]


def case_one():
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    assert (Solution().productExceptSelf(nums)) == output


def case_two():
    nums = [-1, 1, 0, -3, 3]
    output = [0, 0, 9, 0, 0]
    assert (Solution().productExceptSelf(nums)) == output


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
