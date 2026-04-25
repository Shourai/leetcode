class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for i in range(n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


def case_one():
    n = 10
    m = 3
    print(Solution().differenceOfSums(n, m))


def case_two():
    n = 5
    m = 6
    print(Solution().differenceOfSums(n, m))


def case_three():
    n = 5
    m = 1
    print(Solution().differenceOfSums(n, m))


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
