class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures) - 1
        days = []

        left = 0
        right = 1

        while right <= n:
            if temperatures[left] < temperatures[right]:
                days.append(right - left)
                left += 1
                right = left + 1
                continue
            elif left == n - 1 and right == n:
                days.append(0)
                right += 1
                break
            elif temperatures[left] > temperatures[right]:
                right += 1
                continue

        days.append(0)
        return days


def case_one():
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [1, 1, 4, 2, 1, 1, 0, 0]
    assert (Solution().dailyTemperatures(input)) == output


def case_two():
    input = [30, 40, 50, 60]
    output = [1, 1, 1, 0]
    assert (Solution().dailyTemperatures(input)) == output


def case_three():
    input = [30, 60, 90]
    output = [1, 1, 0]
    assert (Solution().dailyTemperatures(input)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
