class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures) - 1
        result = (n + 1) * [0]
        stack = []

        while n >= 0:
            if not stack:
                result[n] = 0
                stack.append(n)
                n -= 1
            elif temperatures[n] < temperatures[stack[-1]]:
                result[n] = stack[-1] - n
                stack.append(n)
                n -= 1
            else:
                stack.pop()

        return result


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
