class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}

        for i in s:
            if i not in counter_s:
                counter_s[i] = 0
            counter_s[i] += 1

        for i in t:
            if i not in counter_t:
                counter_t[i] = 0
            counter_t[i] += 1

        if counter_s == counter_t:
            return True
        return False


def case_one():
    s = "anagram"
    t = "nagaram"
    assert (Solution().isAnagram(s, t)) is True


def case_two():
    s = "rat"
    t = "car"
    assert (Solution().isAnagram(s, t)) is False


def case_three():
    s = "aa"
    t = "a"
    assert (Solution().isAnagram(s, t)) is False


def case_four():
    s = "aacc"
    t = "ccac"
    assert (Solution().isAnagram(s, t)) is False


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
    case_four()
