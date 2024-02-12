class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or pairs[stack.pop()] != bracket:
                return False

        return len(stack) == 0


def case_one():
    s = "()"
    assert (Solution().isValid(s)) is True


def case_two():
    s = "()[]{}"
    assert (Solution().isValid(s)) is True


def case_three():
    s = "(]"
    assert (Solution().isValid(s)) is False


def case_four():
    s = "([)]"
    assert (Solution().isValid(s)) is True


if __name__ == "__main__":
    # case_one()
    # case_two()
    # case_three()
    case_four()
