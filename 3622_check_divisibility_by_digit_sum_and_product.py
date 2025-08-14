import math


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = sum(int(digit) for digit in str(n))
        digit_product = math.prod(int(digit) for digit in str(n))
        if digit_sum + digit_product == 0:
            return False

        print(digit_sum, digit_product, digit_sum + digit_product)
        return n % (digit_sum + digit_product) == 0


def case_one():
    solution = Solution()
    assert solution.checkDivisibility(99) == True
    assert solution.checkDivisibility(23) == False


def case_two():
    solution = Solution()
    assert solution.checkDivisibility(19) == True
    assert solution.checkDivisibility(1234) == False


def case_three():
    solution = Solution()
    assert solution.checkDivisibility(0) == False
    assert solution.checkDivisibility(100) == True


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
