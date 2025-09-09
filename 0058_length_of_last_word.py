class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        string_list = s.split(" ")
        return len(string_list[-1])


def case_one():
    s = "Hello World"
    Solution().lengthOfLastWord(s)


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
