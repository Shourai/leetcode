class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        return string == "".join(reversed(string))


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        arr = [x.lower() for x in s if x.isalnum()]
        return arr == arr[::-1]


def case_one():
    s = "A man, a plan, a canal: Panama"
    output = True
    assert (Solution().isPalindrome(s)) == output


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
