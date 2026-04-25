class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            for digit in str(num):
                digit_sum += int(digit)

        return abs(element_sum - digit_sum)


def case_one():
    input = [1, 15, 6, 3]
    print(Solution().differenceOfSum(input))


def case_two():
    input = [1, 2, 3, 4]
    print(Solution().differenceOfSum(input))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
