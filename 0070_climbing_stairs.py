from functools import lru_cache
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def case_one():
    n = 46
    print(Solution().climbStairs(n))


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
