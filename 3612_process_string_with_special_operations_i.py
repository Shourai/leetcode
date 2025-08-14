class Solution:
    def remove_last_char(self, s: str) -> str:
        return s[:-1]

    def duplicate_string(self, s: str) -> str:
        return s + s

    def reverse_string(self, s: str) -> str:
        return s[::-1]

    def processStr(self, s: str) -> str:
        string = ""
        for ch in s:
            if ch == "*":
                string = self.remove_last_char(string)
            elif ch == "#":
                string = self.duplicate_string(string)
            elif ch == "%":
                string = self.reverse_string(string)
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
