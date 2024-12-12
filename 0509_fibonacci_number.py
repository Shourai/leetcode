class Solution:
    cache = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        else:
            result = self.fib(n-1) + self.fib(n-2)
            self.cache[n] = self.cache[n-1] + self.cache[n-2]
            return result

def case_one():
    n = 10
    output = 1
    print(Solution().fib(n))
    # assert Solution().fib(n) == output

def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
