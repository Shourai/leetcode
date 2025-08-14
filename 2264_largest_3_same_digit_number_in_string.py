class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -1

        def check(num: str) -> bool:
            # check if length is 3 and are all the same numbers
            return len(num) == 3 and num[0] == num[1] == num[2]

        for i in range(0, len(num)):
            window = num[i : i + 3]

            if check(window) and int(window) > largest:
                largest = int(window)

        if largest == -1:
            return ""
        elif largest == 0:
            return "000"
        else:
            return str(largest)


def case_one():
    num = "6777133339"
    solution = Solution()
    print(solution.largestGoodInteger((num)))
    # assert(solution.largestGoodInteger((num)))


def case_two():
    num = "2300019"
    solution = Solution()
    print(solution.largestGoodInteger((num)))


def case_three():
    num = "42352338"
    solution = Solution()
    print(solution.largestGoodInteger((num)))


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
