class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        counter = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                counter += 1
        return counter


def case_one():
    s = "aAbBcC"
    print(Solution().countKeyChanges(s))


def case_two():
    s = "AaAaAaaA"
    print(Solution().countKeyChanges(s))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
