class Solution:
    def processStr(self, s: str) -> str:
        string = ""
        for ch in s:
            if ch == "*":
                string = string[:-1]
            elif ch == "#":
                string += string
            elif ch == "%":
                string = string[::-1]
            else:
                string += ch
        return string


def case_one():
    s = "a#b%*"
    Solution().processStr(s)


def case_two():
    s = "z*#"
    Solution().processStr(s)


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
