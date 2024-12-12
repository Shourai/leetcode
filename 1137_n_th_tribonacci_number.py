class Solution:
    cache = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        else:
            result = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.cache[n] = result
            return result


def case_one():
    n = 4
    output = 4
    assert Solution().tribonacci(n) == output


def case_two():
    n = 25
    output = 1389537
    assert Solution().tribonacci(n) == output


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
