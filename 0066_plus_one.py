class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join(map(str, digits)))
        number += 1

        return list(map(int, list(str(number))))


def case_one():
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
