class Solution:
    def maximum69Number(self, num: int) -> int:
        numbers = [i for i in str(num)]
        for i in range(len(numbers)):
            if numbers[i] == "6":
                numbers[i] = "9"
                return int("".join(numbers))
        return num


def case_one():
    num = 9669
    Solution().maximum69Number(num)


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
