class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        if x == 1:
            return 1

        while left < right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1

        return left - 1


def case_one():
    x = 4
    output = 2
    assert Solution().mySqrt(x) == output


def case_two():
    x = 8
    output = 2
    assert Solution().mySqrt(x) == output


def case_three():
    x = 1
    output = 1
    assert Solution().mySqrt(x) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
