class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        while n != 1:
            digits = list(str(n))
            n = sum([pow(int(digit), 2) for digit in digits])

            if n in seen:
                return False

            seen.append(n)

        return True




# class Solution:
#     def isHappy(self, n: int) -> bool:
#         digits = list(str(n))
#         n = sum([pow(int(digit),2) for digit in digits])
#         if n == 1:
#             return True
#         elif n == 4:
#             return False
#         else:
#             return self.isHappy(n)


def case_one():
    n = 19
    assert Solution().isHappy(n) is True


def case_two():
    n = 2
    assert Solution().isHappy(n) is False


def case_three():
    n = 1
    assert Solution().isHappy(n) is True


def case_four():
    n = 13
    assert Solution().isHappy(n) is True


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
