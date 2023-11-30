class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product: int
        right_product: int

        total = left_product * right_product


def case_one():
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    assert (Solution().productExceptSelf(nums)) == output


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
