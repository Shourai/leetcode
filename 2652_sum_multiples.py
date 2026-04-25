class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(n + 1):
            if i % 3 == 0:
                sum += i
            elif i % 5 == 0:
                sum += i
            elif i % 7 == 0:
                sum += i
        return sum



def case_one():
    n = 7
    print(Solution().sumOfMultiples(n))


def case_two():
    n = 10
    print(Solution().sumOfMultiples(n))


def case_three():
    n = 9
    print(Solution().sumOfMultiples(n))


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
