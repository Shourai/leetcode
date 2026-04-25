class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1
        return count


def case_one():
    hours = [0, 1, 2, 3, 4]
    target = 2
    print(Solution().numberOfEmployeesWhoMetTarget(hours, target))


def case_two():
    hours = [5, 1, 4, 2, 2]
    target = 6
    print(Solution().numberOfEmployeesWhoMetTarget(hours, target))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
